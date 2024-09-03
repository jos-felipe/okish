/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/11 17:09:14 by gfantoni          #+#    #+#             */
/*   Updated: 2024/09/03 11:22:44 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/minishell.h"

static void	mini_no_error_detect(t_mini *mini);
static void	mini_recursive_init(t_mini *mini);

int	main(void)
{
	t_mini	*mini;

	mini = get_mini_address();
	mini_ctrl_signal(mini);
	mini_getenv(mini);
	mini->status = 0;
	while (42)
	{
		mini_recursive_init(mini);
		if (mini->cmd_line == NULL)
		{
			mini_ctrl_d_exit();
			break ;
		}
		if (mini->cmd_line[0] == '\0')
			continue ;
		add_history(mini->cmd_line);
		mini_tokenizer(mini);
		if (!mini->syntax_error && mini->token_list)
			mini_no_error_detect(mini);
	}
	ft_free_trashman(ft_get_mem_address());
	ft_free_trashman_env(ft_get_mem_address_env());
}

void	mini_no_error_detect(t_mini *mini)
{
	mini_parser(mini);
	mini_expansion(mini);
	mini_redirect(mini);
	mini_execute(mini);
}

#include <string.h>
 
#define PROMPT_LEN 11

void	mini_recursive_init(t_mini *mini)
{
	char	msg[PROMPT_LEN + 1];
	char	*last_dir;
	char	*str;
	char	*prompt;
	char	**split_pwd = NULL;
	int		i;
	int		len;
	
	mini_init(mini);
	// memset(msg, '\0', PROMPT_LEN + 1);
	str = ft_dict_get_value(mini->env_list, "PWD");
	len = 0;
	if (str != NULL)
	{
		len = ft_strlen(str);
		split_pwd = ft_split(str, '/');
	}
	if (split_pwd != NULL)
	{
		i = 0;
		while (split_pwd[i])
			last_dir = split_pwd[i++];
	}
	ft_memcpy(msg, last_dir, PROMPT_LEN - 2);
	prompt = ft_strjoin(last_dir, "/$ ");
	// msg[PROMPT_LEN - 2] = '$';
	// msg[PROMPT_LEN - 1] = ' ';
	// i = 0;
	// while (i < PROMPT_LEN - 1 && i < len)
	// {
	// 	msg[PROMPT_LEN - i - 2] = str[len - i - 1];
	// 	i++;
	// }
	
	// msg[i] = '$';
	mini->int_action.sa_handler = sig_handler;
	sigaction(SIGINT, &mini->int_action, NULL);
	mini->quit_action.sa_handler = SIG_IGN;
	sigaction(SIGQUIT, &mini->quit_action, NULL);
	// mini->cmd_line = readline("prompt > ");
	mini->cmd_line = readline(prompt);
	ft_collect_mem(mini->cmd_line);
}
