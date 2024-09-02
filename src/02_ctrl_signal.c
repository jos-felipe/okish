/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   02_ctrl_signal.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gfantoni <gfantoni@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/05 16:42:04 by josfelip          #+#    #+#             */
/*   Updated: 2024/06/18 11:56:31 by gfantoni         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/minishell.h"

void	mini_ctrl_signal(t_mini *mini)
{
	struct sigaction	int_action;
	struct sigaction	quit_action;

	int_action.sa_handler = sig_handler;
	sigemptyset(&int_action.sa_mask);
	int_action.sa_flags = 0;
	sigaction(SIGINT, &int_action, NULL);
	quit_action.sa_handler = SIG_IGN;
	quit_action.sa_flags = 0;
	sigemptyset(&quit_action.sa_mask);
	sigaction(SIGQUIT, &quit_action, NULL);
	mini->int_action = int_action;
	mini->quit_action = quit_action;
}
