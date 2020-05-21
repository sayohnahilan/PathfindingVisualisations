import math
import threading
from random import random
from random import seed

from pygame.locals import *

from searchAlgorithms import *
from pygameBoard import *
from optionsWindow import *

# colours
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

while 1:
    # # main
    # run options window
    app = mainWindow()
    app.mainloop()
    # pull data from options window
    size = app.gameOptions["size"].get()
    fps = app.gameOptions["fps"].get()
    maze = app.gameOptions["maze"].get()
    alg = app.gameOptions["alg"].get()
    startX = app.gameOptions["startX"].get()
    startY = app.gameOptions["startY"].get()
    endX = app.gameOptions["endX"].get()
    endY = app.gameOptions["endY"].get()

    # # dev // uncomment section below to run with dev config
    # sample dev values from options window
    # alg = "Best First Search"
    # maze = "Random Maze"
    # size = 30
    # startX = 1
    # startY = 1
    # endX = 27
    # endY = 27
    # fps = 540

    # initialize board and initial squares
    colorQ = queue.Queue()
    myBoard = Board(size * 20, size * 20, black)
    mySearch = Search(size, size, (startX, startY), (endX, endY), colorQ)
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Visualizing Pathfinding Algorithms')
    myBoard.drawLines(white)
    myBoard.colourOne(startX, startY, blue)
    myBoard.colourOne(endX, endY, blue)

    # draw a maze if the user requests it
    if maze == "Random Maze":
        for i in range(math.floor(size ** 2 * 0.42)):
            seed(i)
            x = math.floor(size * 20 * random() + 1)
            y = math.floor(size * 20 * random() + 1)
            try:
                mouseX, mouseY = myBoard.findSquare(x, y)
                mouseX //= 20
                mouseY //= 20
                if not (mouseX == startX and mouseY == startY) and not (
                        mouseX == endX and mouseY == endY):
                    myBoard.colourOne(mouseY, mouseX, yellow)
                    mySearch.colourMatrix(mouseY, mouseX, yellow)
            except:
                pass
        pygame.display.update()

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
                    gridX = mouseX // 20
                    gridY = mouseY // 20
                    if not (gridX == startX and gridY == startY) and not (
                            gridX == endX and gridY == endY):
                        if mySearch.matrix[gridY][gridX].c == yellow:
                            square = pygame.Rect(mouseX + 1, mouseY + 1, 18, 18)
                            pygame.draw.rect(myBoard.screen, black, square)
                            mySearch.colourMatrix(gridY, mouseX // 20, black)
                        else:
                            myBoard.colourOne(gridY, gridX, yellow)
                            mySearch.colourMatrix(gridY, gridX, yellow)
                except:
                    pass
        pygame.display.update()


    # start a thread which runs the alg
    if alg == "Best First Search":
        myThread = threading.Thread(target=mySearch.bestFirst())
    elif alg == "Dijkstra's Algorithm":
        myThread = threading.Thread(target=mySearch.dijkstra())
    elif alg == "A Star Search":
        myThread = threading.Thread(target=mySearch.aStar())
    elif alg == "Breadth First Search":
        myThread = threading.Thread(target=mySearch.breadthFirstSearch())
    elif alg == "Depth First Search":
        myThread = threading.Thread(target=mySearch.depthFirstSearch())
    myThread.start()


    backTracking = True
    while backTracking:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if colorQ.empty():
                    pygame.quit()
                    backTracking = False
                else:
                    sys.exit()

        # if a colour is added to the queue (by alg), colour it
        if not colorQ.empty():
            x, y, c = colorQ.get()
            myBoard.colourOne(x, y, c)
            pygame.display.update()