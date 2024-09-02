import os

# define user variable
user = os.environ['USER']

def test_collection():

	# Simple
	input_list = ["echo 42"]
	output_ref_list = ["42\n"]
	output_exit_code = ["0\n"]

	input_list.append("< infile_1 cat")
	output_ref_list.append(f"melvin\n")
	output_exit_code.append("0\n")

	# input_list.append("< infile_1 cat | echo")
	# output_ref_list.append(f"\n")
	# output_exit_code.append("0\n")

	input_list.append("")
	output_ref_list.append(f"")
	output_exit_code.append("0\n")

	input_list.append(" ")
	output_ref_list.append(f"")
	output_exit_code.append("0\n")

	input_list.append("echo melvin > outfile_1")
	output_ref_list.append(f"")
	output_exit_code.append("0\n")

	# Export
	input_list.append("export foo=bar\nexport foo=bar2 | echo $foo")
	output_ref_list.append(f"bar\n")
	output_exit_code.append("0\n")

	# File error
	input_list.append("cat > .")
	output_ref_list.append(f"minishell: .: Is a directory\n")
	output_exit_code.append("1\n")

	input_list.append("cat > /")
	output_ref_list.append(f"minishell: /: Is a directory\n")
	output_exit_code.append("1\n")

	input_list.append("cat > usr/local/bin")
	output_ref_list.append(f"minishell: usr/local/bin: No such file or directory\n")
	output_exit_code.append("1\n")

	input_list.append("< no_infile cat")
	output_ref_list.append(f"minishell: no_infile: No such file or directory\n")
	output_exit_code.append("1\n")

	input_list.append("< no_perm_infile cat")
	output_ref_list.append(f"minishell: no_perm_infile: Permission denied\n")
	output_exit_code.append("1\n")

	# Expansion
	input_list.append("echo $nada")
	output_ref_list.append(f"\n")
	output_exit_code.append("0\n")

	input_list.append("$nada")
	output_ref_list.append(f"")
	output_exit_code.append("0\n")

	input_list.append("echo $USER")
	output_ref_list.append(f"{user}\n")
	output_exit_code.append("0\n")

	input_list.append("echo \"$USER\"")
	output_ref_list.append(f"{user}\n")
	output_exit_code.append("0\n")

	input_list.append("echo \'$USER\'")
	output_ref_list.append(f"$USER\n")
	output_exit_code.append("0\n")

	input_list.append("echo $?USER")
	output_ref_list.append("0USER\n")
	output_exit_code.append("0\n")

	input_list.append("echo $abc^def")
	output_ref_list.append("^def\n")
	output_exit_code.append("0\n")

	input_list.append("echo $^def")
	output_ref_list.append("$^def\n")
	output_exit_code.append("0\n")

	input_list.append("echo $USER^def")
	output_ref_list.append(f"{user}^def\n")
	output_exit_code.append("0\n")

	input_list.append("echo oi$USER")
	output_ref_list.append(f"oi{user}\n")
	output_exit_code.append("0\n")

	# Command error
	input_list.append("ERR")
	output_ref_list.append("minishell: ERR: command not found\n")
	output_exit_code.append("127\n")

	input_list.append("\"\"")
	output_ref_list.append("minishell: : command not found\n")
	output_exit_code.append("127\n")

	input_list.append("\'\'")
	output_ref_list.append("minishell: : command not found\n")
	output_exit_code.append("127\n")
	# input_list.append("echo a | ERR b | echo c")
	# output_ref_list.append(f"minishell: ERR: command not found\nc\n")
	# output_exit_code.append("0\n")

	# input_list.append("echo a | echo b | ERR c")
	# output_ref_list.append(f"minishell: ERR: command not found\n")
	# output_exit_code.append("127\n")

	# Syntax error
	input_list.append("echo 'a b")
	output_ref_list.append(f"minishell: syntax error: unterminated quoted string\n")
	output_exit_code.append("2\n")

	input_list.append("|")
	output_ref_list.append(f"minishell: syntax error near unexpected token\n")
	output_exit_code.append("2\n")

	input_list.append("echo a | | echo b")
	output_ref_list.append(f"minishell: syntax error near unexpected token\n")
	output_exit_code.append("2\n")

	input_list.append("echo a > | echo b")
	output_ref_list.append(f"minishell: syntax error near unexpected token\n")
	output_exit_code.append("2\n")

	input_list.append("echo a >>> outfile_1")
	output_ref_list.append(f"minishell: syntax error near unexpected token\n")
	output_exit_code.append("2\n")

	input_list.append("echo a | > outfile_2")
	output_ref_list.append(f"")
	output_exit_code.append("0\n")

	input_list.append("> outfile_3")
	output_ref_list.append(f"")
	output_exit_code.append("0\n")

	input_list.append("export foo\nexport | grep foo")
	output_ref_list.append(f"declare -x foo\n")
	output_exit_code.append("0\n")

	input_list.append("export foo\nenv | grep foo")
	output_ref_list.append(f"")
	output_exit_code.append("1\n")

	return input_list, output_ref_list, output_exit_code