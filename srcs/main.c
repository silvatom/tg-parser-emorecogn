#include "parsecsv.h"

int	validation(int argc, char *argv[]);
t_list	*get_records(int fd);

int	main(int argc, char *argv[])
{
	int		fd;
	char	*line;
	t_list	*csv;
	
	// argc argv validations
	if (validation(argc, argv))
		return (1);
	fd = open(argv[1], O_RDONLY);
	// rm first line
	line = get_next_line(fd);
	free(line);
	// read it, gnl
	csv = get_records(fd);
	while (csv)
	{
		t_data *asdf = csv->content;
		printf("valence: %f\n", asdf->valence);
		csv = csv->next;
	}
	return (0);
}

int	validation(int argc, char *argv[])
{
	if (argc != 2)
	{
		ft_printf("Invalid number of arguments!\n");
		return (1);
	}
	if (access(argv[1], R_OK) != 0)
	{
		perror("");
		return (1);
	}
	return (0);
}

t_list	*get_records(int fd)
{
	char	*line;
	char	**atts;
	t_data	*class;
	t_list	*csv;
	int		i = 0;;

	csv = NULL;
	while (line = get_next_line(fd))
	{
		ft_printf("i = %d\n", i);
		class = malloc(sizeof(t_data));
		atts = ft_split(line, ',');
		class->valence = strtod(atts[0], NULL);
		class->arousal = strtod(atts[1], NULL);
		
		// clean fpath
		char	*tmp;
		tmp = ft_strdup(atts[2]);
		char	**n = ft_split(atts[2], '\r');
		class->fpath = ft_strdup(n[0]);
		free(tmp);
		ft_destroy_matrix(n);
		ft_destroy_matrix(atts);

		// get fname

		// get dir

		// init list
		if (!csv)
			csv = ft_lstnew(class);
		else
			ft_lstadd_back(&csv, ft_lstnew(class));
		free(line);
		i++;
		if (i == 1000)
			break;
	}
	// init_struct
	return (csv);
}