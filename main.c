/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/11 17:09:14 by gfantoni          #+#    #+#             */
/*   Updated: 2024/09/06 15:04:33 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/minishell.h"

static char	*mini_pwd_prompt(t_mini *mini);
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

void	mini_recursive_init(t_mini *mini)
{
	char	*prompt;

	mini_init(mini);
	mini->int_action.sa_handler = sig_handler;
	sigaction(SIGINT, &mini->int_action, NULL);
	mini->quit_action.sa_handler = SIG_IGN;
	sigaction(SIGQUIT, &mini->quit_action, NULL);
	prompt = mini_pwd_prompt(mini);
	mini->cmd_line = readline(prompt);
	free(prompt);
	ft_collect_mem(mini->cmd_line);
}

char	*mini_pwd_prompt(t_mini *mini)
{
	char	*prompt;
	char	*pwd;
	char	*tmp;

	prompt = ft_calloc(PROMPT_LEN + 1, sizeof(char));
	pwd = ft_dict_get_value(mini->env_list, "PWD");
	if (pwd == NULL)
		return (ft_strdup("?/$ "));
	tmp = ft_split_get_last(pwd, '/');
	if (tmp == NULL)
		return (ft_strdup("?/$ "));
	pwd = ft_strjoin(tmp, "/$ ");
	ft_memcpy(prompt, pwd, ft_min(strlen(pwd), PROMPT_LEN));
	free(pwd);
	free(tmp);
	return (prompt);
}
