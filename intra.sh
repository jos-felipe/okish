#!/bin/bash

find . -maxdepth 1 -not -name Makefile -not -name main.c -not -name readline.supp -not -name .git -not -name include -not -name src -not -name lib -not -name . -exec rm -rf {} \;

