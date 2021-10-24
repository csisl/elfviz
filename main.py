from elfman import ELFMan
import click
import cliff


@click.group()
def main():
    pass


@main.command()
@click.option("--file", prompt="path to binary file: ", type=str)
@click.option("--symbol", prompt="symbol: ", type=str)
@click.option("--log", default=None)
def symbol_offset(file, symbol, log):
    myelf = ELFMan(file, log=log)
    offset = myelf.get_symbol_offset(symbol)
    print("[+] offset: {}".format(offset))


@main.command()
@click.option("--file", prompt="path to binary file: ", type=str)
@click.option("--section", prompt="section: ", type=str)
@click.option("--log", default=None)
def section_info(file, section, log):
    myelf = ELFMan(file, log=log)
    header = myelf.get_section_header(section)
    print(header)
    for h in header:
        print("{}:\t{}".format(h, header[h]))


if __name__ == '__main__':
    main()
