import sys
import pygame
from pygame.locals import *
import queue
import threading
from options import *
from board import *
from algorithms import *

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

# # pull data from options window
# alg = app.gameOptions["alg"].get()
# size = app.gameOptions["size"].get()
# startX = app.gameOptions["startX"].get()
# startY = app.gameOptions["startY"].get()
# endX = app.gameOptions["endX"].get()
# endY = app.gameOptions["endY"].get()

# dev
alg = "A Star Search"
size = 30
startX = 1
startY = 1
endX = 15
endY = 15

# initialize board and initial squares
colorQ = queue.Queue()
myBoard = Board(size * 20, size * 20, black)
mySearch = Search(size, size, (startX, startY), (endX, endY), colorQ)
pygame.init()
myBoard.drawLines(white)
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
                mouseX, mouseY = myBoard.findSquare(event.pos[0], event.pos[1])
                square = pygame.Rect(mouseX, mouseY, 20, 20)
                pygame.draw.rect(myBoard.screen, yellow, square)
                mySearch.colourMatrix(mouseY // 20, mouseX // 20, yellow)
            except:
                pass
    pygame.display.update()


# start a thread which runs the alg
if alg == "A Star Search":
    myThread = threading.Thread(target=mySearch.aStar())
elif alg == "Breadth First Search":
    myThread = threading.Thread(target=mySearch.breadthFirstSearch())
elif alg == "Depth First Search":
    myThread = threading.Thread(target=mySearch.depthFirstSearch())
myThread.start()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # if a colour is added to the queue (by alg), colour it
    if not colorQ.empty():
        x, y, c = colorQ.get()
        myBoard.colourOne(x, y, c)
        pygame.display.update()