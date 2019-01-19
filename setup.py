#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install


setup(name='startup_name_generator',
    version='1.0.2',
    description='Generate a domain name for your new startup.',
    author='Larry Neal',
    author_email='nealla@lwneal.com',
    packages=[
        'startup_name_generator',
    ],
    package_data={
        'startup_name_generator': [
            'startup_name_generator/*.txt',
        ],
    },
    install_requires=[
        "flask",
    ],
    scripts=[
        'generate_startup_name',
    ],
    include_package_data=True,
)

