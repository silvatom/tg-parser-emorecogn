#ifndef PARSECSV_H
# define PARSECSV_H

// printf
#include <stdio.h>
// open
# include <fcntl.h>

// mkdir
// access
# include <unistd.h>
// stat
# include <sys/stat.h>

// strtod
# include <stdlib.h>

// strdup
# include <string.h>

# include "libft.h"
# include "dirs_output.h"

# define OUTPUT_DIR "predfiles"

typedef struct s_data
{
	double	valence;
	double	arousal;
	char	*fpath;
	char	*fname;
	char	*dir;
}				t_data;

char	*concat_strings(int n, ...);
// ft_split
// ft_mtxlen
#endif