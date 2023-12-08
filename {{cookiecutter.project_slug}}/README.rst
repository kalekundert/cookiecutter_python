{{ '*' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '*' * cookiecutter.project_name|length }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
   :alt: Last release
   :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
   :alt: Python version
   :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/readthedocs/{{ cookiecutter.project_slug }}.svg
   :alt: Documentation
   :target: https://{{ cookiecutter.project_slug  | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/test.yml?branch=master
   :alt: Test status
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions

.. image:: https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
   :alt: Test coverage
   :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}?branch=master

.. image:: https://img.shields.io/github/last-commit/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}?logo=github
   :alt: Last commit
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
