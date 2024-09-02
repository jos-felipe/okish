# Handle $? which should expand to the exit status of the most recently executed foreground pipeline.

# Stores exit status in memory;
# When find the $? in the command, replace it with the exit status;

import subprocess

def dolar_sign(command, colours, exit_status):

	# Start minishell, get input from 04_input and redirect the output to outfile
	dollar_sign_status = subprocess.run('./04_assertion.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Assertion dolar sign
	if (dollar_sign_status.stdout == '0\n'):
		print(f"{colours[0]}1/1.	OK  {colours[2]}")
	else:
		print(f"{colours[1]}1/1.	KO  {colours[2]}")
		exit_status = 1

	# Valgrind, start minishell, get input from 04_input and redirect the output to /dev/null
	valgrind_status = subprocess.run('./04_valgrind.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Check for leaks
	if (valgrind_status.stdout == '0\n'):
		print(f"{colours[0]}	MOK  {colours[2]}")
	else:
		print(f"{colours[1]}	MKO  {colours[2]}")
		exit_status = 1
		
	return (exit_status)