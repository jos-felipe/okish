/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mini_get_cmd_path.h                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josfelip <josfelip@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/20 14:14:26 by gfantoni          #+#    #+#             */
/*   Updated: 2024/06/17 12:43:01 by josfelip         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef MINI_GET_CMD_PATH_H
# define MINI_GET_CMD_PATH_H

typedef struct s_get_cmd_path
{
	char	*cmd_name;
	char	*path;
	char	*part_path;
	char	**splited_path;
	int		i;
}	t_get_cmd_path;

#endif
