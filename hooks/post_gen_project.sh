#!/usr/bin/env bash
IFS=$'\n\t'; echo
set -xeuo pipefail

# Make a git repository for the project and make the initial commit.

git init
git add .
git commit -m "initial commit"

cat <<EOF > .git/hooks/commit-msg
#!/usr/bin/env sh
commitlint -e \$1
EOF
chmod u+x .git/hooks/commit-msg

cat <<EOF
********************************************************************************
Once you setup a repository on Github, add the following secrets:

- COVERALLS_TOKEN:  https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
- PYPI_TOKEN:       https://pypi.org/manage/account/token/
********************************************************************************
EOF
