#!/usr/bin/env python3

import subprocess

# Valgrind
valgrind = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --suppressions=readline.supp -q --log-file=valgrind.log"

# Colours
GREEN = "\033[32;1m"
RED = "\033[31;1m"
COLOR_LIMITER = "\033[0m"
colours = [GREEN, RED, COLOR_LIMITER]

def unit_parser():

	status = 0

	trash = subprocess.run("make -C parser", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Input Samples:
	input_data_list = ["\"infile < ls -l | wc -l > outfile\""]
	input_data_list.append("\"infile < cat | tr , * | sort | uniq | grep a | tr a-z A-Z | outfile\"")
	input_data_list.append("\"echo 42 || echo 21\"")
	input_data_list.append("\"echo 42 && echo 21\"")

	# Outputs references:
	output_data_list = [f'infile < ls -l \nwc -l > outfile \n']
	output_data_list.append(f'infile < cat \ntr , * \nsort \nuniq \ngrep a \ntr a-z A-Z \noutfile \n')
	output_data_list.append(f'echo 42 || echo 21 \n')
	output_data_list.append(f'echo 42 && echo 21 \n')

	i = 1
	for input_data, output_ref in zip(input_data_list, output_data_list):
		output = subprocess.run(f"{valgrind} ./parser/unit.tester {input_data}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
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

	trash = subprocess.run("make fclean -C parser", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	return status

if __name__ == '__main__':
	status = unit_parser()
	print(f"status: {status}")
	exit(status)