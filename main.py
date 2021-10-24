from elfman import ELFMan
import click


@click.group()
@click.option("--file", prompt="path to binary file: ", type=str)
@click.option("--debug", default=False)
@click.pass_context
def main(ctx, file, debug):
    ctx.obj['FILE'] = file
    ctx.obj['DEBUG'] = debug


@main.command()
@click.option("--symbol", prompt="symbol: ", type=str)
@click.pass_context
def symbol_offset(ctx, symbol):
    myelf = ELFMan(ctx.obj['FILE'], ctx.obj['DEBUG'])
    offset = myelf.get_symbol_offset(symbol)
    print("[+] offset: {}".format(offset))


@main.command()
@click.option("--section", prompt="section: ", type=str)
@click.pass_context
def section_info(ctx, section):
    myelf = ELFMan(ctx.obj['FILE'], ctx.obj['DEBUG'])
    header = myelf.get_section_header(section)
    print(header)
    for h in header:
        print("{}:\t{}".format(h, header[h]))


@main.command()
@click.pass_context
def all_sections(ctx):
    myelf = ELFMan(ctx.obj['FILE'], ctx.obj['DEBUG'])
    myelf.show_sections()


if __name__ == '__main__':
    main(obj={})
