#ifndef GRID_H
#define GRID_H

#include <stack>
#include <vector>
#include <SFML/Graphics.hpp>


struct location {
    int row;
    int col;

    location() {row = 0; col = 0;}
    location(int r, int c) {row = r; col = c;}
};


struct Cell{
    
    bool visited;

    // wall state
    bool left;
    bool right;
    bool top;
    bool bottom;

    location gridPosition; 
    sf::Color color;
};


class Maze{

    // Class enumerations
    enum class AnimateState {START, ITERATE, END};

    // Class constants
    static const int WALL_THICKNESS = 4;
    static const sf::Color WALL_COLOR;
 

public: 
   
    Maze(int rows, int columns, int cellSize);

    void update();

    void draw(sf::RenderWindow& win );

    
private:

    void init(void);
    void generate(void);
    void selectRandomStart(void);
    location chooseNeighbor(void);
    void removeWall(location neighbor);

    void printCell(const Cell& c);
    void printStack();
    

    // data members
    int m_rows;
    int m_columns;
    int m_cellSize;
    std::vector<std::vector<Cell>> m_grid;

    Maze::AnimateState m_state{AnimateState::START};
    Cell* m_currentCell{nullptr};
    std::stack<Cell*> m_stack;

};

#endif 