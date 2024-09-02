#!/usr/bin/env python3

import subprocess
from evaluator_modules import _02_signals
from evaluator_modules import _03_launch_executable
from evaluator_modules import _04_special_parameter

# Exit Status
exit_status = 0

# Make clean and Make
clean = ["make", "clean", "-C", "../"]
subprocess.run(clean, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
make = ["make", "-C", "../"]
subprocess.run(make, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Command
command = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --suppressions=../readline.supp -q ../minishell"

# Colours
GREEN = "\033[32;1m"
RED = "\033[31;1m"
COLOR_LIMITER = "\033[0m"
colours = [GREEN, RED, COLOR_LIMITER]

# Signals
print("Signals")
exit_status = _02_signals.signals(command, colours, exit_status)
print("\n")

# Search and launch executable
print("Launch executable")
exit_status = _03_launch_executable.launch_executable(command, colours, exit_status)
print("\n")

# Dollar Sign
print("Dollar Sign")
exit_status = _04_special_parameter.dolar_sign(command, colours, exit_status)
print("\n")

subprocess.run(clean, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if exit_status == 0:
	print("🎉🎊🌟✨👏🎈🎈👏👏👏🎈🎈👏🌟✨🎉🎊\n")
else:
	print("🛑 ⚠️ ❌ 💥")
exit(exit_status)
