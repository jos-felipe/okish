/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   builtins.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/11 14:28:50 by josfelip          #+#    #+#             */
/*   Updated: 2024/09/06 21:23:13 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef BUILTINS_H
# define BUILTINS_H

# include "../include/minishell.h"

int		mini_cd(t_token *arg, t_dict **dict);
int		mini_env(t_token *arg, t_dict **dict);
int		mini_pwd(void);
void	mini_exit(t_token *arg, int status_last_cmd);

#endif
