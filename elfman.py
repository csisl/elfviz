from elftools.elf.elffile import ELFFile
from typing import BinaryIO

class ELFMan():
    """
    Args:
        file: the binary file to examine

    Attributes:
        file: a stream of data from an binary file
        elffile: the elf file object to represent the binary file
    """

    def __init__(self, file: str):
        self.file = self._get_file(file)
        self.elffile = self._get_elf(self.file)

    def _get_file(self, file: str) -> BinaryIO:
        try:
            open_file = open(file, "rb")
        except Exception as e:
            # TODO: get better exception
            raise("[-] error reading binary file [{}]".format(e))

        return open_file

    def _get_elf(self, file: BinaryIO) -> ELFFile:
        try:
            elffile = ELFFile(file)
        except Exception as e:
            # TODO: get correct exception for files that aren't elfs
            raise("[-] file is not an ELF! [{}]".format(e))

        return elffile

    def get_symbol_offset(self, symbol: str):
        print("[!] looking up symbol {}".format(symbol))

    def __del__(self):
        """
        Make sure we clean up and close the open file
        """
        try:
            self.file.close()
        except:
            pass