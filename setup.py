import os
import platform
import shutil
from setuptools import setup, find_packages


setup(
    name='tst',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tst = core.main:main']
    },

    install_requires=[
        'Colorama',
        'Click',
        'beautifulsoup4',
        'requests',
        'html5lib'
        ]
    )


setup_path = os.getcwd()

system = platform.system()

config_path = ''

match system:
    case 'Linux':
        config_path =  '/etc/tst'
    case 'Windows':
        user_name = os.getlogin()
        config_path = f'C:/Users/{user_name}/AppData/local/Tst'

try:
    os.mkdir(config_path)
    shutil.copy(setup_path+'/core/base.cpp', config_path)
    shutil.copy(setup_path+'/core/config.json', config_path)

except FileExistsError:
    pass

os.chmod(config_path+'/config.json', 0o777)

