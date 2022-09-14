#ifndef PARSECSV_H
# define PARSECSV_H

// printf
#include <stdio.h>
// open
#include <fcntl.h>
// access
#include <unistd.h>
// strtod
#include <stdlib.h>

#include "libft.h"

typedef struct s_data
{
	double	valence;
	double	arousal;
	char	*fpath;
	char	*fname;
	char	*dir;
}				t_data;

#endif