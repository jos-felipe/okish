/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   05_utils_7.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gfantoni <gfantoni@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/18 11:18:42 by gfantoni          #+#    #+#             */
/*   Updated: 2024/06/18 11:40:12 by gfantoni         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/minishell.h"

void	mini_init_hd_signal(t_mini *mini, int *stdin_backup, int *stdout_backup)
{
	*stdin_backup = dup(STDIN_FILENO);
	*stdout_backup = dup(STDOUT_FILENO);
	mini->int_action.sa_handler = sig_handler_heredoc;
	sigaction(SIGINT, &mini->int_action, NULL);
}

void	mini_finish_hd_signal(int *stdin_backup, int *stdout_backup)
{
	dup2(*stdin_backup, STDIN_FILENO);
	dup2(*stdout_backup, STDOUT_FILENO);
	close(*stdin_backup);
	close(*stdout_backup);
}
