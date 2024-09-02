/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gfantoni <gfantoni@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/11 17:09:14 by gfantoni          #+#    #+#             */
/*   Updated: 2024/06/13 15:45:18 by gfantoni         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/minishell.h"

void	unit_print_token_list(t_token *node)
{
	while (node)
	{
		printf("%s;", node->token);
		node = node->next;
	}
}

int main(int argc, char *argv[], char *envp[])
{
	t_mini	mini;

	mini_ctrl_signal(&mini);
	mini_init(&mini);
	mini.cmd_line = argv[1];
	mini_tokenizer(&mini);
	unit_print_token_list(mini.token_list);
	ft_free_trashman(ft_get_mem_address());
	//mini_free_token_list(&mini.token_list); 
	return (0);
}