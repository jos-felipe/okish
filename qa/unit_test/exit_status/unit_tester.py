#!/usr/bin/env python3

import subprocess

# Program name
name = "exit_status"

# Valgrind
valgrind = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --suppressions=readline.supp -q --log-file=valgrind.log"

# Colours
GREEN = "\033[32;1m"
RED = "\033[31;1m"
COLOR_LIMITER = "\033[0m"
colours = [GREEN, RED, COLOR_LIMITER]

def unit_exit_status():

	status = 0

	# Preparing environment.
	trash = subprocess.run(f"make -C {name}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.run("touch executable", shell=True)
	subprocess.run("chmod -x executable", shell=True)
	subprocess.run("mkdir directory", shell=True)
	subprocess.run("cp /usr/bin/ls .", shell=True)
	subprocess.run("chmod -x ls", shell=True)

	# Input Samples:

	# return status = 2: syntax error; wrong command flag
	input_data_list = ["\'echo a | grep -B\'"]
	output_data_list = [f'2\n']

	input_data_list.append("\'|\'")
	output_data_list.append(f'2\n')

	# return status = 126: permission denied; is a directory
	input_data_list.append("\'./executable\'")
	output_data_list.append(f'126\n')

	input_data_list.append("\'./directory\'")
	output_data_list.append(f'126\n')

	input_data_list.append("\'./ls\'")
	output_data_list.append(f'126\n')

	# return status = 127: command not found; no such file or directory
	input_data_list.append("\'echo a | echo b | echoERR c\'")
	output_data_list.append(f'127\n')

	input_data_list.append("\'echo a | echoERR b | echo c\'")
	output_data_list.append(f'c\n0\n')

	input_data_list.append("\'echoERR a\'")
	output_data_list.append(f'127\n')

	input_data_list.append("\'./nada\'")
	output_data_list.append(f'127\n')

	i = 1

	for input_data, output_ref in zip(input_data_list, output_data_list):
		output = subprocess.run(f"{valgrind} ./{name}/unit.tester {input_data}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		outfile_content = output.stdout
		if outfile_content == output_ref:
			print(f"{colours[0]}{i}/{len(input_data_list)}.	OK  {colours[2]}")
		else:
			print(f"{colours[1]}{i}/{len(input_data_list)}.	KO  {colours[2]}")
			status = 1

		valgrind_status = subprocess.run('./valgrind.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

		# Check for leaks
		if (valgrind_status.stdout == '0\n'):
			print(f"{colours[0]}	MOK  {colours[2]}")
		else:
			print(f"{colours[1]}	MKO  {colours[2]}")
			status = 1
		i = i + 1

	trash = subprocess.run(f"rm -rf executable directory ls", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
	trash = subprocess.run(f"make fclean -C {name}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
	
	return status

if __name__ == '__main__':
	status = unit_exit_status()
	print(f"status: {status}")
	exit(status)