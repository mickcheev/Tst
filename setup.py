from setuptools import setup, find_packages

setup(
    name='tst',
    version='1.0',
    packages=['core'],
    entry_points={
        'console_scripts': ['tst = core.main:main']
    }
        )
