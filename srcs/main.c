#include "parsecsv.h"

int	validation(int argc, char *argv[]);
t_list	*get_records(int fd);

int	main(int argc, char *argv[])
{
	int		fd;
	char	*line;
	t_list	*csv = NULL;
	
	// argc argv validations
	if (validation(argc, argv))
		return (1);

    FILE * fp;
    line = NULL;
    size_t len = 0;
    ssize_t read;

	// create output files
	struct stat st = {0};
	if (stat(OUTPUT_DIR, &st) == -1)
		mkdir(OUTPUT_DIR, 0744);
	else
	{
		FILE *fp;
		fp = popen("rm -rf output", "r");
		mkdir(OUTPUT_DIR, 0744);
	}

	// create output dir
	// create files with text

	// open file
    fp = fopen(argv[1], "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);
	
	// change to the directory where the files will be placed
	chdir(OUTPUT_DIR);

	// create files to be written on
	int i = 0;
	int	dirs_qtd = ft_mtxlen(dirs);
	int	fd1;
	while (i < dirs_qtd)
	{
		fd1 = open(dirs[i], O_CREAT | O_RDWR, 0744);
		write(fd1, "valence,arousal\n", 16);
		close(fd1);
		i++;
	}
	i = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);
        // printf("%s", line);

		t_data *class = malloc(sizeof(t_data));

		// split line
		char **atts = ft_split(line, ',');

		// clean fpath
		class->fpath = strndup(atts[2], strlen(atts[2]) - 2);
		class->valence = strtod(atts[0], NULL);
		class->arousal = strtod(atts[1], NULL);

		// get fname
		char **tmp1 = ft_split(class->fpath, '\\');
		class->fname = tmp1[ft_mtxlen(tmp1) - 1];

		// get dir
		class->dir = tmp1[ft_mtxlen(tmp1) - 2];

		char	val_str[100];
		char	aro_str[100];
		snprintf(val_str, 100, "%f", class->valence);
		snprintf(aro_str, 100, "%f", class->arousal);
		char	*str = concat_strings(4, val_str, ",", aro_str, "\n");

		// write in the file
		int	fd2 = open(class->dir, O_RDWR | O_APPEND, 0644);
		write(fd2, str, strlen(str));
		close(fd2);

        free(line);
		line = NULL;
		ft_destroy_matrix(atts);
		ft_destroy_matrix(tmp1);
		free(str);
		// free(class->fpath);
		// free(class->fname);
		// free(class->dir);
    }
	printf("ok\n");
    fclose(fp);
    exit(EXIT_SUCCESS);

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
		perror("asdf");
		return (1);
	}
	return (0);
}