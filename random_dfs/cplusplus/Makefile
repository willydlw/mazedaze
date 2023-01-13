
all: mazegen

mazegen: main.o maze.o
	g++ main.o maze.o -o mazegen -lsfml-graphics -lsfml-window -lsfml-system

main.o: main.cpp
	g++ -Wall -c main.cpp 

maze.o: maze.cpp
	g++ -Wall -c maze.cpp

clean:
	rm *.o mazegen
