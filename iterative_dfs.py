import sys
import pygame
import random

from cell import * 
from grid import *  


def iterative_dfs(maze):

   stack = []

   # 1. Choose the initial cell, mark it as visited
   #    and push it onto the stack
   current = maze.selectRandomStart()
   print("start cell col: ", current.col)
   print("start cell row: ", current.row)
   current.visited = True
   stack.append(current)

   # 2. While the stack is not empty
   while stack:
      # pop a cell from the stack and make it the current cell
      current = stack.pop()

      # if the current cell has any neighbors which have not
      # been visited 
      neighbors = maze.findUnVisitedNeighbors(current)

      if neighbors:
         # push the current cell onto the stack
         stack.append(current)

         # choose one of the unvisited neighbors
         chosen = random.choice(neighbors)

         # remove the wall between the current cell and the chosen cell
         maze.removeWalls(current, chosen)

         # mark the chosen cell as visited and push it to the stack
         chosen.visited = True 

         stack.append(chosen)


   

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

   iterative_dfs(maze)
  

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