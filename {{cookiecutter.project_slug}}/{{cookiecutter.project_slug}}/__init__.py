#!/usr/bin/env python3

__version__ = '0.0.0'
{% if cookiecutter.project_type == 'application' %}
def main():
    print("Hello world!")
{%- endif %}
