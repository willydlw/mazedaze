# mazedaze
Exploring maze generation and solving algorithms


## Maze Generator 

### Randomized Depth-First Seach (aka "recursive backtracker")

Algorithm description, https://en.wikipedia.org/wiki/Maze_generation_algorithm 

"Starting from a random cell, the computer then selects a random neighbouring cell that has not yet been visited. The computer removes the wall between the two cells and marks the new cell as visited, and adds it to the stack to facilitate backtracking. The computer continues this process, with a cell that has no unvisited neighbours being considered a dead-end. When at a dead-end it backtracks through the path until it reaches a cell with an unvisited neighbour, continuing the path generation by visiting this new, unvisited cell (creating a new junction). This process continues until every cell has been visited, causing the computer to backtrack all the way back to the beginning cell." [1](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

[Iterative Implementation](/home/diane/repos/mazedaze/iterative_dfs.py)

1. Choose the initial cell, mark it as visited and push it to the stack
2. While the stack is not empty
   a. Pop a cell from the stack and make it a current cell
   b. If the current cell has any neighbours which have not been visited
      i.   Push the current cell to the stack
      ii.  Choose one of the unvisited neighbours
      iii. Remove the wall between the current cell and the chosen cell
      iv.  Mark the chosen cell as visited and push it to the stack

[Recursive Implementation](/home/diane/repos/mazedaze/recursive_dfs.py)

1. Given a current cell as a parameter
2. Mark the current cell as visited
3. While the current cell has any unvisited neighbor cells
   a. Choose one of the unvisited neighbors
   b. Remove the wall between the current cell and the chosen cell
   c. Invoke the routine recursively for the chosen cell

>Note: The iterative and recursive implementation default values generate a maze of width 642, height 482, cell size 20. For the recursive implementation, changing the cell size to 10 generated the following error: "RecursionError: maximum recursion depth exceeded in comparison" The iterative implementation was able to handle the cell size of 10 during my testing. Your experience may differ, based on your testing environment.
