#!/usr/bin/env python3
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re
with open('{{ cookiecutter.project_slug }}/__init__.py') as file:
    version_pattern = re.compile("__version__ = '(.*)'")
    version = version_pattern.search(file.read()).group(1)
with open('README.rst') as file:
    readme = file.read()

setup(
    name='{{ cookiecutter.project_slug }}',
    version=version,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=[
        '{{ cookiecutter.project_slug }}',
    ],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.main',
        ],
    },
    install_requires=[
    ],
    keywords=[
        '{{ cookiecutter.project_slug }}',
    ],
    include_package_data=True,
    license='MIT',
    zip_safe=False,
)
