#include "maze.h"
#include <iostream>
#include <stack>


// Define Class Constants
const sf::Color Maze::CURRENT_CELL_COLOR = sf::Color::Yellow;
const sf::Color Maze::STACK_CELL_COLOR = sf::Color::Blue;
const sf::Color Maze::START_CELL_COLOR = sf::Color::Green;
const sf::Color Maze::WALL_COLOR = sf::Color::White;
const sf::Color Maze::INIT_CELL_COLOR = sf::Color(75, 75, 75, 50);

Maze::Maze(int rows, int columns, int cellSize) :
    m_rows(rows),
    m_columns(columns),
    m_cellSize(cellSize),
    m_grid(rows, std::vector<Cell>(columns)),
    m_state(AnimateState::START),
    m_currentCell(nullptr)
{
    
    this->init();
}

void Maze::init(void)
{
    for(int r = 0; r < m_rows; ++r)
    {
        for(int c = 0; c < m_columns; c++)
        {
            m_grid[r][c].visited = false;
            m_grid[r][c].left = true;
            m_grid[r][c].right = true;
            m_grid[r][c].top = true;
            m_grid[r][c].bottom = true;
            m_grid[r][c].color = INIT_CELL_COLOR;
            m_grid[r][c].gridPosition.row = r;
            m_grid[r][c].gridPosition.col = c;
        }
    }
}

void Maze::update(void)
{
    switch(m_state)
    {
        case AnimateState::START:
            this->selectRandomStart();
            m_state = AnimateState::ITERATE;
        break;

        case AnimateState::ITERATE:
            if(!m_stack.empty())
            {
                // pop a cell from the stack and make it the current cell
                *m_currentCell = m_stack.top();
                m_stack.pop();

                m_currentCell->color = CURRENT_CELL_COLOR;

                // choose one of the unvisited neighbors
                location nextLocation = chooseNeighbor();

                // if the current cell has any unvisited neighbors
                if(nextLocation.row != -1 && nextLocation.col != -1)
                {
                    // push the current cell to the stack
                    m_stack.push(*m_currentCell);
                    
                    // remove the wall between the current cell and the chosen cell
                    removeWall(nextLocation);

                    // mark the chosen neighbor cell as visited and push it to the stack
                    m_grid[nextLocation.row][nextLocation.col].visited = true;
                    m_grid[nextLocation.row][nextLocation.col].color = STACK_CELL_COLOR;
                    m_stack.push(m_grid[nextLocation.row][nextLocation.col]);
                }
                else
                { // we're done with this cell
                    m_currentCell->color = sf::Color::Black;
                }
            }
            else{  // stack empty
                m_state = AnimateState::END;
            }
        break;
        case AnimateState::END:
        break;
    }
}


void Maze::selectRandomStart()
{
    int row = rand() % m_rows;
    int col = rand() % m_columns;


    std::cout   << "Start Location, row: " << row
                << ", col: " << col << "\n";
    
    m_currentCell = &m_grid[row][col];

    // mark it as visited
    m_currentCell->visited = true;
    m_currentCell->color = START_CELL_COLOR;

    // push it to the stack
    m_stack.push(*m_currentCell);
}


location Maze::chooseNeighbor(void) 
{
    std::vector<location> neighborList;
    location neighborLocation;
    location curLocation = m_currentCell->gridPosition;
    
    /* Neighbor (row, col) index offsets
        Left     0, -1
        Right    0, +1
        Above   -1,  0
        Below   +1,  0 
    */

    // left
    if( (curLocation.col > 0) && !m_grid[curLocation.row][curLocation.col-1].visited)
    {
        neighborLocation.row = curLocation.row;
        neighborLocation.col = curLocation.col-1;
        neighborList.push_back(neighborLocation);
    }

    // right
    if( (curLocation.col < m_columns-1) && !m_grid[curLocation.row][curLocation.col+1].visited)
    {
        neighborLocation.row = curLocation.row;
        neighborLocation.col = curLocation.col+1;
        neighborList.push_back(neighborLocation);
    }

    // above 
    if(curLocation.row > 0 && !m_grid[curLocation.row-1][curLocation.col].visited)
    {
        neighborLocation.row = curLocation.row - 1;
        neighborLocation.col = curLocation.col;
        neighborList.push_back(neighborLocation);
    }

    // below
    if( (curLocation.row < m_rows-1) && !m_grid[curLocation.row+1][curLocation.col].visited)
    {
        neighborLocation.row = curLocation.row + 1;
        neighborLocation.col = curLocation.col;
        neighborList.push_back(neighborLocation);
    }

    if(neighborList.size() > 0)
    {
        int index = std::rand() % neighborList.size();
        neighborLocation = neighborList[index];
    }
    else
    {
        neighborLocation.row = -1;
        neighborLocation.col = -1;
    }
    
    return neighborLocation; 
}




void Maze::removeWall(location neighbor)
{ 
    location current = m_currentCell->gridPosition;
    if(current.col < neighbor.col)
    {
        // current is left of neighbor
        m_grid[current.row][current.col].right = false;
        m_grid[neighbor.row][neighbor.col].left = false;
    }
    else if(current.col > neighbor.col)
    {   
        // current is right of neighbor
        m_grid[current.row][current.col].left = false;
        m_grid[neighbor.row][neighbor.col].right = false;

    }
    else if(current.row < neighbor.row)
    {
        // current is above neighbor
        m_grid[current.row][current.col].bottom = false;
        m_grid[neighbor.row][neighbor.col].top = false;
    }
    else if(current.row > neighbor.row)
    {
        // current is below neighbor
        m_grid[current.row][current.col].top = false;
        m_grid[neighbor.row][neighbor.col].bottom = false;
    }
}






void Maze::printCell(const Cell& c)
{
    std::cout << "visited: " << (c.visited ? "true" : "false") << "\n";
    std::cout << "left: " << (c.left ? "true" : "false") << "\n";
    std::cout << "right: " << (c.right ? "true" : "false") << "\n";
    std::cout << "top: " << (c.top ? "true" : "false") << "\n";
    std::cout << "bottom: " << (c.bottom ? "true" : "false") << "\n\n";
    std::cout << "row:    " << c.gridPosition.row << "\n";
    std::cout << "col:    " << c.gridPosition.col << "\n";
    std::cout << "\n";
} 


 void Maze::draw(sf::RenderWindow& win )
 {
    for(int r = 0; r < m_rows; ++r)
    {
        for(int c = 0; c < m_columns; ++c)
        {
            int x = c * m_cellSize;
            int y = r * m_cellSize;

            // draw rectangle with fill color to indicate cell's state
            sf::RectangleShape rect(sf::Vector2f(m_cellSize, m_cellSize));
            rect.setPosition(x, y);
            rect.setFillColor(m_grid[r][c].color);
            win.draw(rect);

            std::cout << "r: " << r << ", c: " << c << "\n";
            std::cout << "x: " << x << ", y: " << y << "\n";


            if(m_grid[r][c].left){
                sf::RectangleShape wall(sf::Vector2f(WALL_THICKNESS, m_cellSize));
                wall.setPosition(x, y);
                wall.setFillColor(sf::Color::Red);
                win.draw(wall);
            } 

            
            if(m_grid[r][c].right){
                sf::RectangleShape wall(sf::Vector2f(WALL_THICKNESS, m_cellSize));
                wall.setPosition(x + m_cellSize - WALL_THICKNESS, y);
                wall.setFillColor(sf::Color::White);
                win.draw(wall);
            }

            if(m_grid[r][c].top){
                sf::RectangleShape wall(sf::Vector2f(m_cellSize, WALL_THICKNESS));
                wall.setPosition(x, y);
                wall.setFillColor(sf::Color::Yellow);
                win.draw(wall);
            } 

            if(m_grid[r][c].bottom){
                sf::RectangleShape wall(sf::Vector2f(m_cellSize, WALL_THICKNESS));
                wall.setPosition(x, y + m_cellSize - WALL_THICKNESS);
                wall.setFillColor(sf::Color::Green);
                win.draw(wall);
            }
        }
    }
 }

