#!/usr/bin/env python3

import os
import subprocess

os.chdir('../unit_test')

def run_unit_tests():
	output = subprocess.run("/usr/bin/env python3 main.py", shell=True)
	return (output.returncode)
