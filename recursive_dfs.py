import sys
import pygame
import random


class Cell:
   def __init__(self, c, r):
      self.col = c
      self.row = r
      # wall order: left, right, top, bottom
      self.leftWall = True
      self.rightWall = True 
      self.topWall = True 
      self.bottomWall = True 
      self.visited = False

   def show(self, win, cellSize):
      x = self.col * cellSize
      y = self.row * cellSize 

      ##pygame.draw.rect(win, (200,0,0), (x,y,cellSize,cellSize))

      if self.leftWall:
         # surface, color, start pos, end pos, width
         pygame.draw.line(win, (255,255,255), (x,y),(x,y+cellSize), 2)

      if self.rightWall:
         # surface, color, start pos, end pos, width
         pygame.draw.line(win, (255,255,255), (x+cellSize,y),(x+cellSize,y+cellSize), 2)

      if self.topWall:
         # surface, color, start pos, end pos, width
         pygame.draw.line(win, (255,255,255), (x,y),(x+cellSize,y), 2)

      if self.bottomWall:
         pygame.draw.line(win, (255,255,255), (x,y+cellSize),(x+cellSize,y+cellSize), 2)
      


class Grid:
   def __init__(self, columns, rows):
      self.columns = columns
      self.rows = rows 
      self.grid = []
      self.populateGrid()

   def populateGrid(self):
      for r in range(self.rows):
         for c in range(self.columns):
            cell = Cell(c,r)
            self.grid.append(cell)

   def selectRandomStart(self):
      col = random.randrange(self.columns)
      row = random.randrange(self.rows)
      index = self.getGridIndex(col, row)
      return self.grid[index]

   
   def getGridIndex(self, col, row):
      if(col < 0 or row < 0 or col >= self.columns or row >= self.rows):
         return -1
      else:
         return(row * self.columns + col)

   def findUnVisitedNeighbors(self, cell):
      neighbors = []

      # left neighbor is col-1, row
      index = self.getGridIndex(cell.col-1, cell.row)
      
      if index >= 0:
         left = self.grid[index]
         if not left.visited:
            neighbors.append(left)

      # right neighbor is col+1, row
      index = self.getGridIndex(cell.col+1, cell.row)
      if index >= 0:
         right = self.grid[index]
         if not right.visited:
            neighbors.append(right)

      # top neighbor is col, row-1
      index = self.getGridIndex(cell.col, cell.row-1)
      if index >= 0:
         top = self.grid[index]
         if not top.visited:
            neighbors.append(top)

      # bottom neighbor is col, row+1
      index = self.getGridIndex(cell.col, cell.row+1)
      if index >= 0:
         bottom = self.grid[index]
         if not bottom.visited:
            neighbors.append(bottom)

      return neighbors

   def removeWalls(self, a, b):
      # Is next left, right, top, bottom neighbor?
      # left and right neighbors will differ in column values
      x = a.col - b.col
      if x == 1:     # a is to the right of b
         a.leftWall = False
         b.rightWall = False
      elif x == -1:  # a is to the left of b
         a.rightWall = False
         b.leftWall = False

      # top and bottom will differ in row values
      y = a.row - b.row
      if y == 1:     # a is below b
         a.topWall = False
         b.bottomWall = False 
      elif y == -1:  # a is above b
         a.bottomWall = False 
         b.topWall = False 
      

   def show(self, win, cellSize):
      for cell in self.grid:
         cell.show(win, cellSize)



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

   grid = Grid(cols,rows)

   current = grid.selectRandomStart()
   print("start cell col: ", current.col)
   print("start cell row: ", current.row)

   recursive_dfs(current, grid)
  

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      
      win.fill((0,0,0))       # paint background

      grid.show(win,cellSize)

      pygame.display.flip()



if __name__ == "__main__":
   main()