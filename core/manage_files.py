import json
import subprocess
import os

DEFAULT_PATH = '/usr/bin/'

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

def get_default_filename() -> str:
    with open(DEFAULT_PATH + 'config.json', 'r') as file:
        return json.load(file)['default_file_path']

def make_templated_cpp_file(filename: str):
    text = ''
    with open(DEFAULT_PATH+'base.cpp') as file:
        text = file.read()

    subprocess.run(['touch', f'{filename}'])
    
    with open(filename, 'w') as file:
        file.write(text)
    
    set_default_filename(filename)


def make_initialization_files():
    os.system('touch previousfile')
    os.system('touch samples.txt')


    
