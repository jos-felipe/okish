#!/bin/bash

for file in ../../../../src/*; do
  if [[ $(basename "$file") != "00_main.c" ]]; then
    ln "$file" ./
  fi
done