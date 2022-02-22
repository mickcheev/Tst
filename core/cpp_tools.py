import subprocess
import os


from colorama import Fore

from . import manage_files

DEFAULT_SOURCE_NAME = 'main'


def execute_cpp():
    messages = list()
    tests = manage_files.get_sample_list()

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
    prevfn = 'previousfile'

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


