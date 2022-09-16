#include "parsecsv.h"

char	*concat_strings(int n, ...)
{
	char	*str;
	char	*old;
	int		i;
	va_list	args;
	char	*tmp;

	str = ft_strdup("");
	va_start(args, n);
	i = 0;
	while (i < n)
	{
		tmp = va_arg(args, char *);
		old = str;
		str = ft_strjoin(str, tmp);
		free(old);
		i++;
	}
	va_end(args);
	return (str);
}
