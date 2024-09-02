#!/bin/bash

STATUS=0
PID=$(pidof minishell)
kill -s SIGINT $PID
cat outfile | grep "prompt > ^C" > /dev/null
GREP_STATUS=$(echo $?)
if [ "$GREP_STATUS" != "0" ]; then
	STATUS=1
fi
echo $STATUS
