import pygame
from pygame.locals import *
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

while 1:
    # main
    # run options window
    app = mainWindow()
    app.mainloop()
    # pull data from options window
    size = app.gameOptions["size"].get()
    fps = app.gameOptions["fps"].get()
    alg = app.gameOptions["alg"].get()
    startX = app.gameOptions["startX"].get()
    startY = app.gameOptions["startY"].get()
    endX = app.gameOptions["endX"].get()
    endY = app.gameOptions["endY"].get()

    # # dev
    # alg = "Best First Search"
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