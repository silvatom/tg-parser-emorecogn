# MAIN VARS
NAME		=	parsecsv
CC			=	gcc
CFLAGS		=	#-Wall -Werror -Wextra
INCFLAGS	=	-I include $(LIBFT_INC)

# LIB
LIBFT		=	ft
LIBFT_DIR	=	./libft
LIBFT_INC	=	-I libft/includes
INCS_LFT	=	libft.h
LIBFT_LINK	=	-L$(LIBFT_DIR) -l$(LIBFT)

# SRCS
SRCS		=	srcs
MAIN		=	main.c concat_string.c



## VALIDATION
# ARGVAL_DIR	=	argval
# ARGVAL_SRCS	=	arg_validation.c

SRCS_DIR	=	srcs
SRCS		=	$(MAIN)
# $(addprefix $(ARGVAL_DIR)/, $(ARGVAL_SRCS))

# OBJS
OBJS_DIR	=	objs
OBJS		=	$(addprefix $(OBJS_DIR)/, $(SRCS:.c=.o))
DIR_GUARD	=	@mkdir -p $(@D)

SRCS_PATH	=	$(addprefix $(SRCS_DIR)/, $(SRCS))

# EXPLICIT COMPILATION
$(OBJS_DIR)/%.o: $(SRCS_DIR)/%.c include/parsecsv.h
	$(DIR_GUARD)
	$(CC) $(CFLAGS) $(INCFLAGS) -c $< -o $@

$(NAME): $(OBJS)
	@make -C $(LIBFT_DIR)
	$(CC) $(CFLAGS) $(INCFLAGS) $^ $(LIBFT_LINK)  -o $@

all: $(NAME)

clean:
	rm -rf $(OBJS_DIR)
	rm -rf debug

fclean: clean
	@make -C $(LIBFT_DIR) $@
	rm -rf $(NAME) output

re: fclean all

valgrind:

debug: $(SRCS_PATH)
	$(CC) -g $(CFLAGS) $(INCFLAGS) $^ $(LIBFT_LINK)  -o $@
	gdb --tui --args $@ input_files/va_affwild_validation.csv

.PHONY: all clean fclean valgrind debug