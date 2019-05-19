#!/usr/bin/env python3
# encoding: utf-8

from setuptools import setup

with open('README.rst') as file:
    readme = file.read()

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.0.0',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    long_description=readme,
    packages=[
        '{{ cookiecutter.project_slug }}',
    ],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}:main',
        ],
    },
    install_requires=[
    ],
)
