#!/usr/bin/env bash
IFS=$'\n\t'; echo
set -xeuo pipefail

# Make a git repository for the project and make the initial commit.

git init
git add .
git commit -m "chore: apply cookiecutter"

cat <<EOF > .git/hooks/commit-msg
#!/usr/bin/env sh
pccc \$1
EOF
chmod u+x .git/hooks/commit-msg

mkdir tests
cat TODO
