/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libftplus.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 12:59:04 by josfelip          #+#    #+#             */
/*   Updated: 2024/09/06 14:29:30 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFTPLUS_H
# define LIBFTPLUS_H

# include "../lib/includes/libft.h"
# include "trashman.h"

char	*ft_split_get_last(char *str, char sep);
char	*ft_substr_mem(char *str, int start, int len);
size_t	ft_min(size_t a, size_t b);
void	ft_split_free(char **split);

#endif