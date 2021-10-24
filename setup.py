# !/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

PROJECT = 'elfcli'
VERSION = '0.1'

setup(
    name=PROJECT,
    version=VERSION,

    description='CLI for ELF binaries',

    url='https://github.com/csisl/elfviz',

    install_requires=['cliff', 'pyelftools'],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'elfcli = elfcli.main:main'
        ],
        'elif.cli': [
            'sections = elfcli.show:Sections',
        ],
    },

    zip_safe=False,
)