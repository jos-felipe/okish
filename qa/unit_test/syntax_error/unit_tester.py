#!/usr/bin/env python3

import subprocess

# Valgrind
valgrind = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --suppressions=readline.supp -q --log-file=valgrind.log"

# Colours
GREEN = "\033[32;1m"
RED = "\033[31;1m"
COLOR_LIMITER = "\033[0m"
colours = [GREEN, RED, COLOR_LIMITER]

def unit_syntax_error():

	status = 0

	trash = subprocess.run("make -C syntax_error", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Input Samples

	# Pipe errors:
	input_data_list = ["\"a b | c d\""]
	input_data_list.append("\"a b|c d\"")
	input_data_list.append("\"a b |\"")
	input_data_list.append("\"a b|\"")
	input_data_list.append("\"| c d\"")
	input_data_list.append("\"|c d\"")
	input_data_list.append("\"|\"")
	input_data_list.append("\"  |  \"")

	# Consecutives operators errors
	input_data_list.append("\"echo a | | echo b\"")
	input_data_list.append("\"echo melvin | > outfile\"")
	input_data_list.append("\"echo melvin >>> outfile\"")
	input_data_list.append("\"echo melvin > | cat\"")
	input_data_list.append("\"echo melvin >> | cat\"")
	input_data_list.append("\"echo melvin >| cat\"")
	input_data_list.append("\"echo melvin >>| cat\"")
	input_data_list.append("\"echo melvin <<< melvin\"")
	input_data_list.append("\"echo melvin <<<< melvin\"")
	input_data_list.append("\"echo melvin > < melvin\"")
	input_data_list.append("\"echo melvin > << melvin\"")
	input_data_list.append("\"echo melvin > <<< melvin\"")

	# Outputs references:
	output_data_list = [[f'', "C"]]
	output_data_list.append([f'', "C"])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])

	output_data_list.append([f'', "C"])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])
	output_data_list.append(["E", f'minishell: syntax error near unexpected token\n'])


	i = 1
	for input_data, output_ref in zip(input_data_list, output_data_list):
		output = subprocess.run(f"{valgrind} ./syntax_error/unit.tester {input_data}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		outfile_content = output.stdout
		if output_ref[0] == "E":
			outfile_content = output.stderr
			output_ref = output_ref[1]
		else:
			output_ref = output_ref[0]
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

	trash = subprocess.run("make fclean -C syntax_error", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	return status

if __name__ == '__main__':
	status = unit_syntax_error()
	print(f"status: {status}")
	exit(status)