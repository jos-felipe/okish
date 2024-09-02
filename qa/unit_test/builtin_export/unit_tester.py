#!/usr/bin/env python3

# https://www.gnu.org/savannah-checkouts/gnu/bash/manual/html_node/Bourne-Shell-Builtins.html#index-export

import subprocess
import difflib

def string_difference(s1, s2):
	differ = difflib.Differ()
	diff = differ.compare(s1.splitlines(), s2.splitlines())
	for line in diff:
		if line.startswith('+') or line.startswith('-'):
			print(line)

def unit_export():
	status = 0

	# Valgrind
	valgrind = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --suppressions=readline.supp -q --log-file=valgrind.log"

	# Colours
	GREEN = "\033[32;1m"
	RED = "\033[31;1m"
	COLOR_LIMITER = "\033[0m"
	CYAN = "\033[36;1;3;208m"
	YELLOW = "\033[33;1m"
	colours = [COLOR_LIMITER, RED, GREEN, CYAN, YELLOW]

	trash = subprocess.run("make -C builtin_export", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Test description, Input Samples and Outputs references:

	#1
	test_description_list = [" - null value"]
	input_data_list = ["\'export var\' \'echo $var\'"]
	output_data_list = [f' ']
	err_data_list = [f'']
	exit_status_list = [0]

	#2
	test_description_list.append(" - single word")
	input_data_list.append("\'export var=jojo\' \'echo $var\'")
	output_data_list.append(f'jojo ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	test_description_list.append(" - multiple words")
	input_data_list.append("\'export var=jojo kaka\' \'echo $var\'")
	output_data_list.append(f'jojo ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	test_description_list.append(" - null value variant")
	input_data_list.append("\'export var=\' \'echo $var\'")
	output_data_list.append(f' ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	test_description_list.append(" - invalid identifier with value")
	input_data_list.append("\'export =jojo\'")
	output_data_list.append(f'')
	err_data_list.append(f'export: not a valid identifier\n')
	exit_status_list.append(1)

	test_description_list.append(" - invalid identifier without value")
	input_data_list.append("\'export =\'")
	output_data_list.append(f'')
	err_data_list.append(f'export: not a valid identifier\n')
	exit_status_list.append(1)

	test_description_list.append(" - multiple variables")
	input_data_list.append("\'export var1=kaka var2=jojo\' \'echo $var1 $var2\'")
	output_data_list.append(f'kaka jojo ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	test_description_list.append(" - multiple variables plus invalid identifier")
	input_data_list.append("\'export var1 var2=jojo =\' \'echo $var1 $var2\'")
	output_data_list.append(f' jojo ')
	err_data_list.append(f'export: not a valid identifier\n')
	exit_status_list.append(1)

	test_description_list.append(" - update variable content")
	input_data_list.append("\'export LANG=pt\' \'echo $LANG\'")
	output_data_list.append(f'pt ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	test_description_list.append(" - don't update if null address")
	input_data_list.append("\'export _myvar_\' \'echo $_myvar_\'")
	output_data_list.append(f' ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	test_description_list.append(" - update if null value")
	input_data_list.append("\'export LANG=\' \'echo $LANG\'")
	output_data_list.append(f' ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	# test_description_list.append(" - assign value using expansion")
	# input_data_list.append("\'export var=$LANG\' \'echo $var\'")
	# output_data_list.append(f'en_US.UTF-8 ')
	# err_data_list.append(f'')
	# exit_status_list.append(0)

	test_description_list.append(" - assign value using invalid expansion")
	input_data_list.append("\'export var=$affsdf\' \'echo $var\'")
	output_data_list.append(f' ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	test_description_list.append(" - variable name starting with number")
	input_data_list.append("\'export 1var=jojo\' \'echo $1var\'")
	output_data_list.append(f' ')
	err_data_list.append(f'export: not a valid identifier\n')
	exit_status_list.append(1)

	test_description_list.append(" - variable name ending with number")
	input_data_list.append("\'export var1=jojo\' \'echo $var1\'")
	output_data_list.append(f'jojo ')
	err_data_list.append(f'')
	exit_status_list.append(0)

	# test_description_list.append(" - export with no options")
	# input_data_list.append("\'export SHLVL=2\' \'export\'")
	# export_status = subprocess.run('bash -c "export"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
	# output_data_list.append(export_status.stdout)
	# err_data_list.append(f'')
	# exit_status_list.append(0)

	# waiting for fix on "" tokenizier
	test_description_list.append(" - export with quotes")
	input_data_list.append("\'export var=\"jojo kaka\"\' \'echo $var\'")
	output_data_list.append(f'jojo kaka ')
	err_data_list.append(f'')
	exit_status_list.append(0)
	#
	# input_data_list.append("\'export \"\"\' \'echo $var\'")
	# output_data_list.append(f' export: not a valid identifier')

	i = 1
	print(f"{colours[3]}*** builtin_export unit test ***{colours[0]}")
	for input_data, output_ref, err_ref in zip(input_data_list, output_data_list, err_data_list):
		output = subprocess.run(f"./builtin_export/unit.tester {input_data}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		outfile_content = output.stdout
		errfile_content = output.stderr
		print(f"{colours[3]}{i}/{len(input_data_list)}{test_description_list[i-1]}{colours[0]}")
		if outfile_content == output_ref and errfile_content == err_ref and output.returncode == exit_status_list[i-1]:
			print(f"{colours[2]}	OK{colours[0]}")
		else:
			print(f"{colours[1]}	KO{colours[0]}")
			if outfile_content != output_ref:
				print(f"{colours[4]}stdout Diff{colours[0]}")
				print(string_difference(output_ref, outfile_content))
				status = 1
			if errfile_content != err_ref:
				print(f"{colours[4]}stderr Diff{colours[0]}")
				print(string_difference(err_ref, errfile_content))
				status = 1
			if output.returncode != exit_status_list[i-1]:
				print(f"{colours[4]}exit status{colours[0]}")
				print(f"Expected: {exit_status_list[i-1]}")
				print(f"Got: {output.returncode}")
				status = 1
		
		# Check for leaks
		subprocess.run(f"{valgrind} ./builtin_export/unit.tester {input_data}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		valgrind_status = subprocess.run(f"./valgrind.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		if (valgrind_status.stdout == '0\n'):
			print(f"{colours[2]}	MOK{colours[0]}")
		else:
			print(f"{colours[1]}	MKO{colours[0]}")
			status = 1
		i = i + 1

	trash = subprocess.run("make fclean -C builtin_export", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	return status

unit_export()