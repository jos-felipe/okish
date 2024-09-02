#!/bin/bash

rm outfile
PID=$(pidof minishell)
kill $PID
