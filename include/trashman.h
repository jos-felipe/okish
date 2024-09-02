/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   trashman.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/11 14:44:19 by josfelip          #+#    #+#             */
/*   Updated: 2024/04/11 15:08:23 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef TRASHMAN_H
# define TRASHMAN_H

# include "../lib/includes/libft.h"

t_list	**ft_get_mem_address(void);
void	ft_collect_mem(void *content);
void	ft_free_trashman(t_list **lst_memory);

#endif