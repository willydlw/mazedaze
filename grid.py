import random 
from cell import * 

class Grid:
   def __init__(self, columns, rows):
      self.columns = columns
      self.rows = rows 
      self.grid = []
      self.populateGrid()

   def populateGrid(self):
      for r in range(self.rows):
         for c in range(self.columns):
            gCell = Cell(c,r)
            self.grid.append(gCell)

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

   def findUnVisitedNeighbors(self, gCell):
      neighbors = []

      # left neighbor is col-1, row
      index = self.getGridIndex(gCell.col-1, gCell.row)
      if index >= 0:
         left = self.grid[index]
         if not left.visited:
            neighbors.append(left)

      # right neighbor is col+1, row
      index = self.getGridIndex(gCell.col+1, gCell.row)
      if index >= 0:
         right = self.grid[index]
         if not right.visited:
            neighbors.append(right)

      # top neighbor is col, row-1
      index = self.getGridIndex(gCell.col, gCell.row-1)
      if index >= 0:
         top = self.grid[index]
         if not top.visited:
            neighbors.append(top)

      # bottom neighbor is col, row+1
      index = self.getGridIndex(gCell.col, gCell.row+1)
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
