CC = clang
CFLAGS = -Wall -Wextra -Werror -Wpedantic

sum5frac: sum5frac.o
	$(CC) -o sum5frac sum5frac.o

sum5frac.o: sum5frac.c
	$(CC) $(CFLAGS) -c sum5frac.c

clean:
	rm -f sum5frac sum5frac.o
