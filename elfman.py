from elftools.common.exceptions import ELFParseError
from elftools.construct import Container
from elftools.elf.elffile import ELFFile
from typing import BinaryIO
import logging

from elftools.elf.sections import Symbol, Section


class ELFMan:
    """
    Args:
        file: the binary file to examine

    Attributes:
        file: BinaryIO  - a stream of data from an binary file
        elffile: ELFFile - the elf file object to represent the binary file
        symtab: SymbolTableSection - the symbol table object
        header: Container - the ELF header
    """
    SYMTAB: str = ".symtab"
    ST_VALUE: str = "st_value"
    ST_SHNDX: str = "st_shndx"

    def __init__(self, file: str, debug=False):
        self.file = ELFMan.get_file(file)
        self.elffile = ELFMan.get_elf(self.file)
        self.symtab = self.elffile.get_section_by_name(ELFMan.SYMTAB)
        self.header = self.elffile.header
        if debug:
            self._enable_debug()

    def _enable_debug(self):
        logging.basicConfig(level=logging.DEBUG)

    @staticmethod
    def get_file(file: str) -> BinaryIO:
        try:
            open_file = open(file, "rb")
        except IOError as e:
            raise("[-] error reading binary file [{}]".format(e))

        return open_file

    @staticmethod
    def get_elf(file_stream: BinaryIO) -> ELFFile:
        try:
            elffile = ELFFile(file_stream)
        except ELFParseError as e:
            raise("[-] file is not an ELF! [{}]".format(e))

        return elffile

    def show_sections(self):
        for section in self.elffile.iter_sections():
            print(section.name)

    def show_symbols(self):
        for symbol in self.symtab.iter_symbols():
            print(symbol.name)

    def show_segments(self):
        # TODO: make me pretty
        for segment in self.elffile.iter_segments():
            print(segment.header)

    def show_elf_header(self):
        for h in self.header:
            print("{}:\t{}".format(h, self.header[h]))

    def get_section_symbol_in(self, symbol: str) -> Section:
        """
        Get the section the symbol is in by determining the index of the
        section, and obtaining the section via index
        """
        section_index = self.get_section_index_by_symbol(symbol)
        section = self.get_section_by_index(section_index)
        logging.debug("[!] symbol [ {} ] in section: {}".format(symbol, section.name))
        return section

    def get_section_index_by_symbol(self, symbol: str) -> int:
        """
        Get the section index of the symbol with the `st_shndx` field
        """
        entry = self.get_symbol_entry(symbol)
        index = entry.get(ELFMan.ST_SHNDX)
        logging.debug("[!] symbol at section index {}".format(index))
        return index

    def get_section_by_index(self, index: int) -> Section:
        """
        Get the section at the index of `index`
        """
        ii = 1
        for section in self.elffile.iter_sections():
            if ii == index:
                return section
            ii += 1

        raise Exception("[-] section index not found: {}".format(index))

    def get_section_header(self, section: str) -> Container:
        header = self.elffile.get_section_by_name(section).header
        return header

    def get_symbol_entry(self, symbol: str) -> Container:
        """
        Get the entry object for the provided symbol. This is a Container with
        the following fields:
          - st_name
          - st_info
          - st_other
          - st_shndx
          - st_size
        """
        symbol_data: Symbol = self.symtab.get_symbol_by_name(symbol)

        if symbol_data is None:
            raise TypeError("[-] no symbol: {}".format(symbol))

        symbol_entry = symbol_data[0].entry

        return symbol_entry

    def get_symbol_address(self, symbol: str) -> int:
        """
        Get the address for the provided symbol
        """
        entry = self.get_symbol_entry(symbol)
        symbol_address = int(entry.get(ELFMan.ST_VALUE))
        logging.debug("[!] symbol address: {}".format(hex(symbol_address)))
        return symbol_address

    def get_symbol_offset(self, symbol: str) -> int:
        """
        Get the offset of a symbol in a file with the following formula:
        symbol address - section address + section offset in file
        """
        symbol_address = self.get_symbol_address(symbol)
        section = self.get_section_symbol_in(symbol)
        section_address = self._get_section_addr(section)
        section_offset = self._get_section_offset(section)

        symbol_offset = symbol_address - section_address + section_offset
        return symbol_offset

    def _get_section_addr(self, section: Section) -> int:
        section_addr = int(section.header.sh_addr)
        logging.debug("[!] section address: {}".format(hex(section_addr)))
        return section_addr

    def _get_section_offset(self, section: Section) -> int:
        return section.header.sh_offset

    def __del__(self):
        """
        Make sure we clean up and close the open file
        """
        try:
            self.file.close()
        except IOError:
            pass
