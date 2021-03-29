import pygame 

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
 