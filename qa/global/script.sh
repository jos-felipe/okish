#!/bin/bash

STATUS=0
../../minishell < file > outfile 2>&1
grep -v "prompt > " outfile | head -n -1 > result
grep -v "prompt > " outfile | tail -n 1  > status_result
RESULT=$(diff result ref_file) 
if [ "$RESULT" ]; then
	STATUS=1
fi
echo $STATUS