from elfman import ELFMan
import sys

# for testing purposes get a variety of known symbols
known_syms = ["open", "mmap", "malloc.o"]

if __name__ == '__main__':
    myelf = ELFMan("examples/hello")
    # sec = myelf.get_section_address(".symtab")
    offset = myelf.get_symbol_offset("open")
    print("offset of open: {}".format(offset))
