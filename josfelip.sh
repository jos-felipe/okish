#!/bin/bash

find . sources lib includes \( -name "*.c" -or -name "*.h" -or -name Makefile \) -exec sed -e 's/gfantoni/josfelip/; s/<gfantoni@student.42sp.org.br>/<josfelip@student.42sp.org.br>/' {} --in-place \;

rm -rf .github
rm -rf .gitignore
rm -rf qa
rm README.md
rm LICENSE
rm gfantoni.sh
rm josfelip.sh
rm checker_linux
rm *.pdf