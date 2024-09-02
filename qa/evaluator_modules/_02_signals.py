# Checks keybord interrupt signals in minishell prompt.: 
# ^C = gives user a new prompt
# ^D = exits prompt
# ^\ = does nothing

# How to send keyboard signals to a subprocess in Python?
# proc.send_signal(signal.SIGINT)
# proc.send_signal(signal.SIGQUIT)
# proc.stdin.close()

import subprocess

def signals(command, colours, exit_status):

	# Start minishell and redirect the output to outfile
	unused_trash = subprocess.Popen('./run_minishell.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	# Send SIGINT to minishell and check if it gives a new prompt
	ctrl_c_status = subprocess.run('./ctrl-c.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Assert the C-c output
	print("	CTRL-C")
	if (ctrl_c_status.stdout == '0\n'):
		print(f"{colours[0]}1/3.	OK  {colours[2]}")
	else:
		print(f"{colours[1]}1/3.	KO  {colours[2]}")
		exit_status = 1

	# Send SIGQUIT to minishell and check if it doesn't quit with core dump
	ctrl_backslash_status = subprocess.run('./ctrl-backslash.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Assert the C-\ output
	if (ctrl_backslash_status.stdout == '0\n'):
		print(f"{colours[0]}2/3.	OK  {colours[2]}")
	else:
		print(f"{colours[1]}2/3.	KO  {colours[2]}")
		exit_status = 1

	# Kill minishell process and remove the outfile
	sh_status = subprocess.run('./kill.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	# Start the minishell program as a subprocess.
	process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	exit_output_ref = "prompt > exit\n"
	# Emulating C-d keystroke
	process.stdin.close()
	exit_output = process.stdout.readline()

	# Get valgrind output
	valgrind_output = process.stderr.readline()

	# Assert the C-d output
	if (exit_output == exit_output_ref):
		print(f"{colours[0]}3/3.	OK  {colours[2]}")
	else:
		print(f"{colours[1]}3/3.	KO  {colours[2]}")
		exit_status = 1
	if valgrind_output == '':
		print(f"{colours[0]}	MKO{colours[2]}")
	else:
		print(f"{colours[1]}	MOK{colours[2]}")
		exit_status = 1

	# Kill minishel process.
	unused_trash = subprocess.run('pkill minishell', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	return (exit_status)