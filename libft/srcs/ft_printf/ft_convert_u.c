/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_u.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: anjose-d <anjose-d@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/10/04 00:33:29 by anjose-d          #+#    #+#             */
/*   Updated: 2022/04/12 18:02:09 by anjose-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

static int	ft_print_u(long long nbr, long long base_n, t_subspec *flags);
static int	ft_u_size(long long nbr, long long base_n);

int	ft_convert_u(t_uint nbr, t_uint base_n, t_subspec *flags)
{
	int				len_p;
	size_t			nbr_len;

	len_p = 0;
	nbr_len = ft_u_size(nbr, base_n);
	if (flags->precision > nbr_len || (flags->is_dot && nbr == 0))
		nbr_len = flags->precision;
	if (flags->is_space || flags->is_psign)
		nbr_len++;
	if (flags->width > nbr_len)
	{
		if (flags->is_msign)
		{
			len_p += ft_print_u(nbr, base_n, flags);
			len_p += ft_print_width(' ', flags->width - len_p);
			return (len_p);
		}
		else if (flags->is_zero && !flags->is_dot)
			flags->precision += flags->width;
		else
			len_p += ft_print_width(' ', flags->width - nbr_len);
	}
	len_p += ft_print_u(nbr, base_n, flags);
	return (len_p);
}

static int	ft_print_u(long long nbr, long long base_n, t_subspec *flags)
{
	int		len_p;
	size_t	nbr_len;

	nbr_len = ft_u_size(nbr, base_n);
	len_p = 0;
	if (flags->is_space)
		len_p += write (1, " ", 1);
	if (flags->is_psign)
		len_p += write(1, "+", 1);
	if (flags->is_space)
		nbr_len++;
	if (nbr_len < flags->precision)
		len_p += ft_print_width('0', flags->precision - nbr_len);
	if (nbr == 0 && flags->is_dot && flags->precision == 0)
		return (0);
	len_p += ft_print_number(nbr, base_n, "0123456789");
	return (len_p++);
}

static int	ft_u_size(long long nbr, long long base_n)
{
	size_t	ret;

	if (nbr == 0)
		return (1);
	ret = 0;
	while (nbr > 0)
	{
		nbr /= base_n;
		ret++;
	}
	return (ret);
}
