/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   95_builtin_cd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/20 14:34:02 by josfelip          #+#    #+#             */
/*   Updated: 2024/09/10 00:24:46 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/builtins.h"
#include "../include/dictionary.h"
#include "../include/minishell.h"

static int	chdir_and_env_sync(t_dict *dict, char *directory);
static int	token_lstsize(t_token *lst);

int	mini_cd(t_token *arg, t_dict **dict)
{
	char	*directory;

	directory = NULL;
	if (!arg)
		directory = ft_dict_get_value(*dict, "HOME");
	else
	{
		if (token_lstsize(arg) != 1)
		{
			ft_putstr_fd("error: cd: bad arguments\n", STDERR_FILENO);
			return (EXIT_FAILURE);
		}
		if (!ft_strncmp(arg->token, "-", ft_strlen(arg->token)))
		{
			directory = ft_dict_get_value(*dict, "OLDPWD");
			ft_printf_fd(STDOUT_FILENO, "%s\n", directory);
		}
		else
			directory = arg->token;
	}
	return (chdir_and_env_sync(*dict, directory));
}

static int	chdir_and_env_sync(t_dict *dict, char *directory)
{
	int		ret;
	char	*var[2];

	var[0] = "OLDPWD";
	var[1] = getcwd(NULL, 0);
	ft_collect_mem_env(var[1]);
	ret = chdir(directory);
	if (ret == -1)
	{
		ft_printf_fd(STDERR_FILENO, \
		"error: cd: cannot change directory to %s\n", \
		directory);
		return (EXIT_FAILURE);
	}
	ft_dict_update(dict, var);
	var[0] = "PWD";
	var[1] = getcwd(NULL, 0);
	ft_collect_mem_env(var[1]);
	ft_dict_update(dict, var);
	return (EXIT_SUCCESS);
}

int	token_lstsize(t_token *lst)
{
	size_t	i;

	i = 0;
	while (lst)
	{
		lst = lst->next;
		i++;
	}
	return (i);
}
