import os
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
config_path =  '/etc/tst'

try:
    os.mkdir(config_path)
    shutil.copy(setup_path+'/core/base.cpp', config_path)
    shutil.copy(setup_path+'/core/config.json', config_path)

except FileExistsError:
    pass

os.chmod(config_path+'/config.json', 0o777)

