#!/bin/bash

STATUS=0
VALGRIND_LOG=valgrind.log
VALGRIND_STATUS=$(cat $VALGRIND_LOG)
if [ "$VALGRIND_STATUS" ]; then
	STATUS=1
fi
echo $STATUS
rm -f $VALGRIND_LOG
