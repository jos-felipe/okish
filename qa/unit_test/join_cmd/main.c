/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gfantoni <gfantoni@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/11 17:09:14 by gfantoni          #+#    #+#             */
/*   Updated: 2024/06/13 15:44:33 by gfantoni         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/minishell.h"

void	unit_print_cmd_exec_word(char **cmd_exec)
{
	int	i;

	i = 0;
	if (cmd_exec)
	{
		while (cmd_exec[i])
		{
			printf("%s ", cmd_exec[i]);
			i++;
		}
	}
}

void	unit_print_cmd_exec_list(t_cmd **head)
{
	t_cmd *node;

	node = *head;
	while (node)
	{
		unit_print_cmd_exec_word(node->cmd_exec);
		printf("\n");
		node = node->next;
	}
}

int main(int argc, char *argv[], char *envp[])
{
	t_mini	mini;

	mini_ctrl_signal(&mini);
	mini_init(&mini);
	mini_getenv(&mini);
	mini.cmd_line = argv[1];
	mini_tokenizer(&mini);
	mini_parser(&mini);
	mini_expansion(&mini);
	mini_redirect(&mini);
	mini_build_cmd_exec(&mini);
	unit_print_cmd_exec_list(&mini.cmd_exec_list);
	ft_free_trashman(ft_get_mem_address());
	ft_free_trashman_env(ft_get_mem_address_env());
	return (0);
}