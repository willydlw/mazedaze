// g++ main.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system

#include <SFML/Graphics.hpp>
#include <iostream>

#include "maze.h"


int main()
{
    // Add 2 extra pixels to draw line for right and bottom borders
    const int WINDOW_WIDTH = 200; //680;
    const int WINDOW_HEIGHT = 250; //480;
    const int cellSize = 50; //68;
    const int rows = WINDOW_HEIGHT / cellSize;
    const int cols = WINDOW_WIDTH / cellSize;

    std::cout << __FUNCTION__ << ", rows: " << rows << ", cols: " << cols << "\n";
    
    sf::RenderWindow window(sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), 
                                "Iterative DFS Maze");

    window.setFramerateLimit(1);
   
    Maze maze(rows, cols, cellSize);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        maze.update();
       
        window.clear();
        maze.draw(window);
        window.display();
    }

    return 0;
}