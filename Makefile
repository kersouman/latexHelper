CC=gcc
CFLAGS= -O3 -W
LDFLAGS= 
SOURCES= creator.c main.c 
EXECNAME= test

all:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(EXECNAME) $(SOURCES) 

clean:
	rm -f *.o core $(EXECNAME)



