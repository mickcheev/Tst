import click

from . import parse_codeforces
from .import cpp_tools
from .import manage_files

from .exceptions import TstException


@click.command('run', help='Start (compile) executable file and test it using samples at Samples.txt')
@click.option('--filename', default=manage_files.get_default_filename(), help='Set the default execute file')
def run_source(filename: str):
    try:
        cpp_tools.compile_cpp(filename)
    except TstException as ex:
        print(ex.message())

    for mes in cpp_tools.execute_cpp():
            print(mes)


@click.command('set-default', help='Makes file executable')
@click.argument('filename')
def set_default_filename_command(filename: str):
    manage_files.set_default_filename(filename)


@click.command('new', help='Makes a cpp file, which have tamplate code and makes it default executable file')
@click.argument('filename')
def makefile(filename: str):
    manage_files.make_templated_cpp_file(filename)


@click.command('init', help='Makes dependency files')
def init_files():
    manage_files.make_initialization_files()


@click.command('link', help='Parses samples from codeforces')
@click.argument('url_link')
def get_samples(url_link: str):
    try:
        parse_codeforces.write_samples(url_link)
    except TstException as ex:
        print(ex.message())


@click.group(help="This programm allows you to automitize compilation and testing\
        of your programms")
def main():
    pass


main.add_command(set_default_filename_command)
main.add_command(run_source)
main.add_command(init_files)
main.add_command(makefile)
main.add_command(get_samples)

if __name__ == '__main__':
    main()
