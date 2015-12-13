#!/usr/bin/env bash
IFS=$'\n\t'; echo
set -xeuo pipefail

# Make a git repository for the project and make the initial commit.

git init
git add .
git commit -m "Initial commit."

# Create a virtual environment and install the new library in it.

virtualenv -p python3 env
env/bin/pip install bumpversion know_its_ok sphinx
env/bin/pip install -e .

# Encrypt you PyPI password for Travis CI.

travis encrypt --add deploy.password -r {{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

