from elftools.common.exceptions import ELFParseError
from elftools.construct import Container
from elftools.elf.elffile import ELFFile
from typing import BinaryIO

from elftools.elf.sections import Symbol, SymbolTableIndexSection, Section


class ELFMan:
    """
    Args:
        file: the binary file to examine

    Attributes:
        file: BinaryIO  -a stream of data from an binary file
        elffile: ELFFile - the elf file object to represent the binary file
        symtab: SymbolTableSection - the symbol table object
    """
    SYMTAB: str = ".symtab"
    ST_VALUE: str = "st_value"
    ST_SHNDX: str = "st_shndx"

    def __init__(self, file: str):
        self.file = ELFMan.get_file(file)
        self.elffile = ELFMan.get_elf(self.file)
        self.symtab = self.elffile.get_section_by_name(ELFMan.SYMTAB)

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

    def get_section_symbol_in(self, symbol: str) -> Section:
        """
        Get the section the symbol is in by determining the index of the
        section, and obtaining the section via index
        """
        section_index = self.get_section_index_by_symbol(symbol)
        section = self.get_section_by_index(section_index)
        return section

    def get_section_index_by_symbol(self, symbol: str) -> int:
        """
        Get the section index of the symbol with the `st_shndx` field
        """
        elf_sym = self.get_symbol_entry(symbol)
        return elf_sym.get(ELFMan.ST_SHNDX)

    def get_section_by_index(self, index: int) -> Section:
        """
        Get the section at index `index`
        """
        ii = 1
        for section in self.elffile.iter_sections():
            if ii == index:
                return section
            ii += 1

    def get_section_header(self, section: Section) -> Container:
        return section.header

    def get_section_addr(self, section: Section) -> int:
        return int(section.header.sh_addr)

    def get_section_offset(self, section: Section) -> int:
        return section.header.sh_offset

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
        elf_sym: Symbol = self.symtab.get_symbol_by_name(symbol)[0]
        return elf_sym.entry

    def get_symbol_address(self, symbol: str) -> int:
        """
        Get the address for the provided symbol
        """
        entry = self.get_symbol_entry(symbol)
        addr_val = entry.get(ELFMan.ST_VALUE)
        return int(addr_val)

    def get_symbol_offset(self, symbol: str) -> int:
        """
        Get the offset of a symbol in a file with the following formula:
        symbol address - section address + section offset in file
        """
        sym_addr = self.get_symbol_address(symbol)
        section = self.get_section_symbol_in(symbol)
        section_addr = self.get_section_addr(section)
        section_offset = self.get_section_offset(section)
        sym_offset = sym_addr - section_addr + section_offset
        return sym_offset

    def show_sections(self):
        for section in self.elffile.iter_sections():
            print(section.name)

    def show_symbols(self):
        for symbol in self.symtab.iter_symbols():
            print(symbol.name)

    def __del__(self):
        """
        Make sure we clean up and close the open file
        """
        try:
            self.file.close()
        except:
            pass