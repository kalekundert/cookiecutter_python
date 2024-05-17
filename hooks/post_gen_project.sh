#!/usr/bin/env bash
IFS=$'\n\t'; echo
set -xeuo pipefail

# Make a git repository for the project and make the initial commit.

git init
git add .
git commit -m "chore: apply cookiecutter"

gitlint install-hook
pre-commit install

mkdir tests
cat TODO
