#!/usr/bin/env python3

import subprocess

# Program name
name = "execute"

# Valgrind
valgrind = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --suppressions=readline.supp -q --log-file=valgrind.log"


def unit_execute():
	
	status = 0

	# Colours
	GREEN = "\033[32;1m"
	RED = "\033[31;1m"
	COLOR_LIMITER = "\033[0m"
	colours = [GREEN, RED, COLOR_LIMITER]

	# Preparing environment.
	trash = subprocess.run(f"make -C {name}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.run("touch infile", shell=True)
	subprocess.run("echo apple, banana, carrot, bread > infile", shell=True)

	# Input Samples:
	input_data_list = ["\'cat < infile > outfile\'"]
	output_data_list = [f'apple, banana, carrot, bread\n']

	input_data_list.append("\'cat -e < infile > outfile\'")
	output_data_list.append(f'apple, banana, carrot, bread$\n')

	input_data_list.append("\'echo melvin | echo guinga > outfile\'")
	output_data_list.append(f'guinga\n')

	input_data_list.append("\'cat < infile -e | tr , . | tr a-z A-Z > outfile\'")
	output_data_list.append(f'APPLE. BANANA. CARROT. BREAD$\n')

	i = 1

	for input_data, output_ref in zip(input_data_list, output_data_list):
		trash = subprocess.run(f"{valgrind} ./{name}/unit.tester {input_data}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		output = subprocess.run(f"cat outfile", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
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

	trash = subprocess.run(f"rm infile outfile", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
	trash = subprocess.run(f"make fclean -C {name}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	return status

if __name__ == '__main__':
	status = unit_execute()
	print(f"status: {status}")
	exit(status)