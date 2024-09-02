#!/bin/bash

STATUS=0
PID=$(pidof minishell)
kill -s SIGQUIT $PID
cat outfile | grep "quit (core dumped)" > /dev/null
GREP_STATUS=$(echo $?)
if [ "$GREP_STATUS" == "0" ]; then
	STATUS=1
fi
echo $STATUS
