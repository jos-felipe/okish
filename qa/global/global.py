#!/usr/bin/env python3

import subprocess

from test_collection import test_collection

# Colours
GREEN = "\033[32;1m"
RED = "\033[31;1m"
COLOR_LIMITER = "\033[0m"
colours = [GREEN, RED, COLOR_LIMITER]

# exit status
exit_status = 0

# Make
trash = subprocess.run("make -C ../../", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Remove log_file
subprocess.run("rm log_file", shell=True)

# Prepare environment
subprocess.run("touch infile_1 no_perm_infile && echo melvin > infile_1 && chmod -r no_perm_infile", shell=True)

# Get test collection lists
input_list, output_ref_list, output_exit_code = test_collection()

# Define command to get exit status
command_exit_code = "\necho $?"

# Iteration
i = 1
for command, reference, reference_exit_code in zip(input_list, output_ref_list, output_exit_code):    

	# Open minishell input file, reference file and status reference file
    with open("file", "w") as file:
        file.write(command + command_exit_code)
    with open("ref_file", "w") as ref_file:
        ref_file.write(reference)
    with open("status_ref_file", "w") as status_ref_file:
        status_ref_file.write(reference_exit_code)

    # Run minishell via script.sh: ../../minishell < file > outfile 2>&1
    output = subprocess.run("./script.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if (output.stdout == '0\n'):
        print(f"{colours[0]}{i}/{len(input_list)}.\n	OK  {colours[2]}")
    else:
        print(f"{colours[1]}{i}/{len(input_list)}.\n	KO  {colours[2]}")
        exit_status = 1

	# Run valgrind via valgrind.sh 
    valgrind_status = subprocess.run('./valgrind.sh', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if (valgrind_status.stdout == '0\n'):
        print(f"{colours[0]}	MOK  {colours[2]}")
    else:
        print(f"{colours[1]}	MKO  {colours[2]}")
        exit_status = 1

	# Compare status result and status reference via status.sh
    status = subprocess.run("./status.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if (status.stdout == '0\n'):
        print(f"{colours[0]}	EOK  {colours[2]}")
    else:
        print(f"{colours[1]}	EKO  {colours[2]}")
        exit_status = 1

	# Build log_file
    with open("result", "r") as result_file:
        result_command = result_file.read()
    with open("status_result", "r") as status_result_file:
        status_result = status_result_file.readlines()[-1]
    with open("log_file", "a") as log_file:
        log_file.write(f"{i}.\ncommand:\n{command}\n\nexpected output:\n{reference}\noutput received:\n{result_command}\nexpected status: {reference_exit_code}status received: {status_result}-------------------------------------------------\n\n")

    i = i + 1

# Display log_file in the output
# subprocess.run("cat log_file", shell=True)

# Clean directory
file_paths = ["outfile", "file", "ref_file", "status_ref_file", "result",  "status_result", "valgrind.log", "outfile_2", "outfile_3", "infile_1", "no_perm_infile"]
rm_command = ["rm", "-f"] + file_paths
subprocess.run(rm_command)

print(f"status: {exit_status}\n")
exit(exit_status)
