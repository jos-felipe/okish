/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   05_utils_2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gfantoni <gfantoni@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/30 11:38:07 by gfantoni          #+#    #+#             */
/*   Updated: 2024/06/18 11:21:59 by gfantoni         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/minishell.h"

void	mini_print_sintax_error_message(int state)
{
	if (state == 200)
		ft_printf_fd(STDERR_FILENO, "minishell: syntax error: \
unterminated quoted string\n");
	else if (state == 201)
		ft_printf_fd(STDERR_FILENO, "minishell: syntax error \
near unexpected token\n");
	else if (state == 202)
		ft_printf_fd(STDERR_FILENO, "minishell: syntax error: \
not a bonus project '||'\n");
}

void	mini_cut_string(t_mini *mini, t_dfa *dfa)
{
	dfa->value = ft_substr(mini->cmd_line, dfa->start,
			(dfa->i - dfa->start) + 1 - dfa->quote);
	ft_collect_mem(dfa->value);
	mini_token_lstadd_back(&mini->token_list,
		mini_token_lstnew(dfa->value, dfa->state));
	dfa->state = 0;
	dfa->quote = 0;
}

void	mini_set_syntax_error(t_mini *mini)
{
	ft_printf_fd(STDERR_FILENO, "minishell: syntax error \
near unexpected token\n");
	mini->syntax_error = 1;
	mini->status = 2;
}
