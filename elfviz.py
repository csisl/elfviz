import IPython as IPython

from elfman import ELFMan
import click


@click.group()
@click.argument("file", type=str)
@click.option("--debug", is_flag=True)
@click.pass_context
def main(ctx, file, debug):
    ctx.obj['FILE'] = file
    ctx.obj['DEBUG'] = debug
    ctx.obj['ELF'] = ELFMan(file, debug)


@main.command()
@click.pass_context
def elf_header(ctx):
    ctx.obj['ELF'].show_elf_header()


@main.command()
@click.argument("symbol", type=str)
@click.pass_context
def symbol_offset(ctx, symbol):
    offset = ctx.obj['ELF'].get_symbol_offset(symbol)
    print("[+] offset: {}".format(offset))


@main.command()
@click.argument("symbol", type=str)
@click.pass_context
def symbol_address(ctx, symbol):
    address = ctx.obj['ELF'].get_symbol_address(symbol)
    print("[+] address: {}".format(hex(address)))


@main.command()
@click.argument("symbol", type=str)
@click.pass_context
def symbol_entry(ctx, symbol):
    entry = ctx.obj['ELF'].get_symbol_entry(symbol)
    for e in entry:
        print("{}:\t{}".format(e, entry[e]))


@main.command()
@click.argument("section", type=str)
@click.pass_context
def section_header(ctx, section):
    header = ctx.obj['ELF'].get_section_header(section)
    for h in header:
        print("{}:\t{}".format(h, header[h]))


@main.command()
@click.pass_context
def all_sections(ctx):
    ctx.obj['ELF'].show_sections()


@main.command()
@click.pass_context
def all_segments(ctx):
    ctx.obj['ELF'].show_segments()


@main.command()
@click.pass_context
def interactive(ctx):
    elf = ctx.obj['ELF']
    IPython.start_ipython(argv=[], user_ns=locals())


if __name__ == '__main__':
    main(obj={})
