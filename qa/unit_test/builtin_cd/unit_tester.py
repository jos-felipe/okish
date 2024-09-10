#!/usr/bin/env python3

# Unit name - the same as the directory name
unit = 'builtin_cd'
builtin = 'cd'

# Design reference
# https://www.gnu.org/savannah-checkouts/gnu/bash/manual/html_node/Bourne-Shell-Builtins.html#index-cd

import subprocess

class CommandRunner:
	def __init__(self):
		self.test_description_list = []
		self.args_list = []
		self.stdout_list = []
		self.stderr_list = []
		self.returncode_list = []

	def run_command_with_input(self, test_description, args):
		self.test_description_list.append(test_description)
		self.args_list.append(args)
		
		# Get the stdout
		cmd_line = f"bash -c \'pwd -P; {builtin} -P {args}; pwd -P\'"
		returned_instance = subprocess.run(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		self.stdout_list.append(returned_instance.stdout)
		
		# Get the stderr
		cmd_line = f"bash -c \'{builtin} {args}\'"
		returned_instance = subprocess.run(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		self.stderr_list.append(returned_instance.stderr)
		
		# Get the return code
		# cmd_line = f"bash -c \'{builtin} {args}; echo $?\'"
		cmd_line = f"{builtin} {args}"
		returned_instance = subprocess.run(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		# returncode = int(returned_instance.stdout)
		returncode = returned_instance.returncode
		self.returncode_list.append(returncode)

def unit_cd():
	# Return code
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

	trash = subprocess.run(f"make -C {unit}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	# Test description, Input Samples and Outputs references:

	command_runner = CommandRunner()

	command_runner.run_command_with_input("directory is not supplied", "")
	command_runner.run_command_with_input("‘..’ appears in directory", "..")
	command_runner.run_command_with_input("regular directory", "/tmp")
	command_runner.run_command_with_input("directory is ‘-’", "-")

	# Legacy
	test_description_list = command_runner.test_description_list
	args_list = command_runner.args_list
	stdout_list = command_runner.stdout_list
	stderr_list = command_runner.stderr_list
	returncode_list = command_runner.returncode_list

	# Check for stdout, stderr and exit status
	i = 1
	print(f"{colours[3]}*** {unit} unit test ***{colours[0]}")
	for arg, output_ref, err_ref in zip(args_list, stdout_list, stderr_list):
		# Open files
		outfile = open(f"{unit}/outfile", "w")
		outfile_ref = open(f"{unit}/outfile_ref", "w")
		errfile = open(f"{unit}/errfile", "w")
		errfile_ref = open(f"{unit}/errfile_ref", "w")
		
		# Run the unit
		cmd_line = f"./{unit}/unit.tester \'pwd\' \'{builtin} {arg}\' \'pwd\'"
		output = subprocess.run(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		outfile.write(f"{output.stdout}\n")
		outfile_ref.write(f"{output_ref}\n")
		errfile.write(f"{output.stderr}\n")
		errfile_ref.write(f"{err_ref}\n")

		# Close files
		outfile.close()
		outfile_ref.close()
		errfile.close()
		errfile_ref.close()
		
		
		print(f"{colours[3]}{i}/{len(args_list)} - {test_description_list[i-1]}{colours[0]}")

		# Check for stdout
		diff_returned = subprocess.run(f"diff {unit}/outfile_ref {unit}/outfile", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		if diff_returned.returncode != 0:
			print(f"{colours[1]}	KO - stdout{colours[0]}")
			print(f"{colours[4]}stdout diff{colours[0]}")
			print(f"{diff_returned.stdout}")
			status = 1
		else:
			print(f"{colours[2]}	OK - stdout{colours[0]}")

		# Check for stderr
		diff_returned = subprocess.run(f"diff {unit}/errfile_ref {unit}/errfile", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		if diff_returned.returncode != 0:
			print(f"{colours[1]}	KO - stderr{colours[0]}")
			print(f"{colours[4]}stderr diff{colours[0]}")
			print(f"{diff_returned.stdout}")
			status = 1
		else:
			print(f"{colours[2]}	OK - stderr{colours[0]}")

		# Check for exit status
		if output.returncode != returncode_list[i-1]:
			print(f"{colours[4]}	KO - exit status{colours[0]}")
			print(f"{colours[4]}exit status diff{colours[0]}")
			print(f"Expected: {returncode_list[i-1]}")
			print(f"Got: {output.returncode}")
			status = 1
		else:
			print(f"{colours[2]}	OK - exit status{colours[0]}")
		
		# Check for leaks
		cmd_line = f"{valgrind} ./{unit}/unit.tester \'{builtin} {arg}\'"
		subprocess.run(cmd_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		valgrind_status = subprocess.run(f"./valgrind.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
		if (valgrind_status.stdout == '0\n'):
			print(f"{colours[2]}	MOK{colours[0]}")
		else:
			print(f"{colours[1]}	MKO{colours[0]}")
			status = 1
		print("\n------------------------------------\n")
		i = i + 1

	# Clean
	subprocess.run(f"rm {unit}/outfile {unit}/outfile_ref {unit}/errfile {unit}/errfile_ref", shell=True)
	trash = subprocess.run(f"make fclean -C {unit}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

	return status

def main():
	unit_cd()

if __name__ == "__main__":
	main()