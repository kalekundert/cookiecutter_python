{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

[![Last release](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Python version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Documentation](https://img.shields.io/readthedocs/{{ cookiecutter.project_slug }}.svg)](https://{{ cookiecutter.project_slug  | replace("_", "-") }}.readthedocs.io/en/latest/)
[![Test status](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/test.yml?branch=master)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![Test coverage](https://img.shields.io/codecov/c/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](https://app.codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![Last commit](https://img.shields.io/github/last-commit/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}?logo=github)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
