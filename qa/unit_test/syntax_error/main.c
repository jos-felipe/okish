/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gfantoni <gfantoni@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/11 17:09:14 by gfantoni          #+#    #+#             */
/*   Updated: 2024/06/13 15:45:08 by gfantoni         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/minishell.h"

int main(int argc, char *argv[], char *envp[])
{
	t_mini	mini;

	mini_ctrl_signal(&mini);
	mini_init(&mini);
	mini.cmd_line = argv[1];
	mini_tokenizer(&mini);
	//printf("%d", mini.syntax_error);
	ft_free_trashman(ft_get_mem_address());
	//mini_free_token_list(&mini.token_list); 
	return (0);
}