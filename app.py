import pygame
from options import *
from board import *

# colours
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

# run options window
app = mainWindow()
app.mainloop()

# pull data from options window
startX = app.gameOptions["startX"].get()
startY = app.gameOptions["startY"].get()
endX = app.gameOptions["endX"].get()
endY = app.gameOptions["endY"].get()

# initialize board and initial squares
myBoard = Board(800, 800, white)
pygame.init()
myBoard.drawLines(black)
myBoard.colourOne(startX, startY, blue)
myBoard.colourOne(endX, endY, blue)
pygame.display.update()