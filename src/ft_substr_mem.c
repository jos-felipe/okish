/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr_mem.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 13:01:36 by josfelip          #+#    #+#             */
/*   Updated: 2024/09/06 15:05:00 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libftplus.h"

char	*ft_substr_mem(char *str, int start, int len)
{
	char	*sub;

	sub = ft_substr(str, start, len);
	ft_collect_mem(sub);
	return (sub);
}

void	ft_split_free(char **split)
{
	int	i;

	i = 0;
	while (split[i])
	{
		free(split[i]);
		i++;
	}
	free(split);
}

char	*ft_split_get_last(char *str, char sep)
{
	char	*last;
	char	**split;
	int		i;

	last = NULL;
	i = 0;
	split = ft_split(str, sep);
	if (split != NULL)
	{
		while (split[i])
			last = split[i++];
	}
	if (last != NULL)
		last = ft_strdup(last);
	ft_split_free(split);
	return (last);
}

size_t	ft_min(size_t a, size_t b)
{
	size_t	min;

	min = a;
	if (min > b)
		min = b;
	return (min);
}
