#!/usr/bin/python

import os
import subprocess
import json
import click

from colorama import init, Fore

import parse_codeforces


DEFAULT_PATH = '/usr/bin/'
DEFAULT_SOURCE_NAME = 'main'

def set_default_filename(filename: str):
    data = {}
    with open(DEFAULT_PATH + 'config.json','r') as file:
        data = json.load(file)

    data['default_file_path'] = filename


    with open(DEFAULT_PATH + 'config.json','w') as file:
        data = json.dump(data, file)

def get_sample_list() -> list[str]:
    result = []
    with open('samples.txt') as file:
        text = file.read()
        now = ''
        prev = ''
        for i in text:
            if i == '\n' and prev == '\n':
                result.append(now)
                now = ''
            else:
                now += i
            prev = i
    return result

def execute_cpp():
    messages = list()
    tests = get_sample_list()

    for i in range(0, len(tests)-1, 2): 
        try:
                    process = subprocess.run([f'./{DEFAULT_SOURCE_NAME}'],
                    capture_output=True,
                    input=tests[i], text=True, timeout=1)
        except subprocess.TimeoutExpired :            
            messages.append(Fore.RED + f'Test {(i+2)//2}: Time limit 1s!\nSample: ' + tests[i])
            continue
        else:
            output = process.stdout.strip()
            if output!=tests[i+1].strip():
                messages.append(Fore.RED + f'Test {(i+2)//2}: Wrong answer!\n' + Fore.RESET
                        + f'Sample: {tests[i]}\nYour answer: \n {output}\nCorrect answer: \n {tests[i+1]}')
                continue
        messages.append(Fore.GREEN + f'Test {(i+2)//2}: OK!')
    return messages

def compile_cpp(filename: str) -> bool:
    prevfn = 'prevfilename'

    with open(prevfn) as file:
        file1_data = file.read()

    with open(filename) as file:
        file2_data = file.read()
    
    if file2_data != file1_data or not os.path.exists(DEFAULT_SOURCE_NAME):
        with open(prevfn, 'w') as file:
            file.write(file2_data)
    
        if os.path.exists(DEFAULT_SOURCE_NAME):
            os.system(f'rm {DEFAULT_SOURCE_NAME}')

        subprocess.run([f'g++' , f'{filename}', '-o', f'{DEFAULT_SOURCE_NAME}'], shell=False, capture_output=True)

        if not os.path.exists(f'{DEFAULT_SOURCE_NAME}'):
            print(Fore.RED + 'Is seems you have a compilation error')
            return False
    return True


def get_default_filename() -> str:
    with open(DEFAULT_PATH + 'config.json', 'r') as file:
        return json.load(file)['default_file_path']


@click.command('run', help='Start (compile) executable file and test it using samples at Samples.txt')
@click.option('--filename', default=get_default_filename(), help='Set the default execute file')
def run_source(filename: str):
    if not os.path.exists(filename):
            print(Fore.RED + 'You set file that does not exist in this directory')
            return None

    file_extension = filename.split('.')[-1]
    
    match file_extension:
        case 'cpp':
            if compile_cpp(filename):
                for mes in execute_cpp():
                    print(mes)


@click.command('set-default', help='Makes file executable')
@click.argument('filename')
def set_default_filename_command(filename: str):
    set_default_filename(filename)

@click.command('new', help='Makes a cpp file, which have tamplate code and makes it default executable file')
@click.argument('filename')
def makefile(filename: str):
    text = ''
    with open(DEFAULT_PATH+'base.cpp') as file:
        text = file.read()

    subprocess.run(['touch', f'{filename}'])
    
    with open(filename, 'w') as file:
        file.write(text)
    
    set_default_filename(filename)


@click.command('init', help='Makes dependency files')
def init_files():
    os.system('touch prevfilename')
    os.system('touch samples.txt')

@click.command('link', help='Parses samples from codeforces')
@click.argument('url_link')
def get_samples(url_link: str):
    samples = parse_codeforces.parse_cf_task_tests(content=parse_codeforces\
            .download_cf_task(url_link))

    final_content = ''

    for sample_test in samples:
        final_content += sample_test.input_text + '\n'
        final_content += sample_test.output_text + '\n'


    with open('samples.txt', 'w') as file:
        file.write(final_content)

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
