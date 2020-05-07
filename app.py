import sys
import pygame
from pygame.locals import *
from options import *
from board import *

# colours
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

# # run options window
# app = mainWindow()
# app.mainloop()
#
# # pull data from options window
# startX = app.gameOptions["startX"].get()
# startY = app.gameOptions["startY"].get()
# endX = app.gameOptions["endX"].get()
# endY = app.gameOptions["endY"].get()

# dev
startX = 1
startY = 1
endX = 36
endY = 36

# initialize board and initial squares
myBoard = Board(800, 800, white)
pygame.init()
myBoard.drawLines(black)
myBoard.colourOne(startX, startY, blue)
myBoard.colourOne(endX, endY, blue)

# Add walls
mouseX = 0
mouseY = 0
startVisualizing = False
drawingWalls = False
while not startVisualizing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                startVisualizing = True
        elif event.type == MOUSEBUTTONDOWN:
            drawingWalls = True
        elif event.type == MOUSEBUTTONUP:
            drawingWalls = False

        if drawingWalls:
            try:
                mouseX, mouseY = event.pos
                mouseX, mouseY = myBoard.findSquare(mouseX, mouseY)
                square = pygame.Rect(mouseX, mouseY, 20, 20)
                pygame.draw.rect(myBoard.screen, yellow, square)
                pygame.display.update()
            except:
                pass
    pygame.display.flip()

print("sayohn exited")