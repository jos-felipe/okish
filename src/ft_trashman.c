/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_trashman.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/29 12:44:33 by gfantoni          #+#    #+#             */
/*   Updated: 2024/06/19 11:33:39 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/trashman.h"

t_list	**ft_get_mem_address(void)
{
	static t_list	*ptr;

	return (&ptr);
}

void	ft_collect_mem(void *content)
{
	ft_lstadd_back(ft_get_mem_address(), ft_lstnew(content));
}

void	ft_free_trashman(t_list **lst_memory)
{
	t_list	*next;

	while (*lst_memory)
	{
		next = (*lst_memory)->next;
		free((*lst_memory)->content);
		free(*lst_memory);
		*lst_memory = next;
	}
	*lst_memory = NULL;
}
