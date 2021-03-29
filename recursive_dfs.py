import sys
import pygame
import random


from cell import * 
from grid import *     


def recursive_dfs(currentCell, grid):
   # 1. Given current cell as a parameter
   # 2. Make the current cell as visited
   currentCell.visited = True 
   
   # while the current cell has any unvisited neighbor cells
   neighbors = grid.findUnVisitedNeighbors(currentCell)

   while len(neighbors) > 0:
      # randomly choose one of the unvisited neighbors
      n = random.choice(neighbors)

      # remove the wall between the current cell and the chosen cell
      grid.removeWalls(currentCell, n)

      # invoke the routine recursively for a chosen cell
      recursive_dfs(n, grid)

      neighbors.clear()
      neighbors = grid.findUnVisitedNeighbors(currentCell)
      


def main():
   pygame.init()
   # add 2 for bottom and right line width display
   win = pygame.display.set_mode((642,482))

   # cells will be square, same width and height
   cellSize = 20

   # Number of columns and rows in grid depend on window
   # dimensions and cell size
   cols = win.get_width()//cellSize
   rows = win.get_height()//cellSize

   maze = Grid(cols,rows)

   current = maze.selectRandomStart()
   print("start cell col: ", current.col)
   print("start cell row: ", current.row)

   recursive_dfs(current, maze)
  

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      
      win.fill((0,0,0))       # paint background

      maze.show(win,cellSize)

      pygame.display.flip()



if __name__ == "__main__":
   main()