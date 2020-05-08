import queue
import heapq
import sys

white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]


class Node:
    c = black
    parent = (0, 0)
    g = sys.maxsize  # cost
    h = 0
    f = 0  # = g + h


class Search:
    def __init__(self, x, y, start, end, colorQ):
        self.x = x
        self.y = y
        self.start = start
        self.end = end
        self.colorQ = colorQ
        self.atEndNode = False
        self.matrix = [[Node() for i in range(x)] for j in range(y)]

    # setter for a matrix location
    def colourMatrix(self, x, y, c):
        self.matrix[x][y].c = c
        self.matrix[x][y].g = sys.maxsize

    # return the nodes beside a start node
    def nodeNeighbors(self, node, diag):
        x, y = node
        if diag == True:
            adj = [(x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1),
                   (x - 1, y - 1)]
        else:
            adj = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        adj = filter(self.onScreen, adj)
        return adj

    # check if neighbor nodes are in confinement
    def onScreen(self, node):
        x, y = node
        if 0 <= x < self.x and 0 <= y < self.y:
            return True
        else:
            return False

    def aStar(self):
        # a queue to store nodes to check / travel to next
        priorityQueue = []
        heapq.heapify(priorityQueue)
        heapq.heappush(priorityQueue, (0, self.start))
        closed = {}

        # start node cost = 0
        self.matrix[self.start[0]][self.start[1]].g = 0

        # for every node in queue
        while not len(priorityQueue) == 0:

            # look for lowest F cost square and move to closed list
            node = heapq.heappop(priorityQueue)[1]
            closed[node] = True
            i, j = node

            # colour the current node red
            self.colorQ.put((i, j, red))

            # stop if end has been found
            if node == self.end:
                self.atEndNode = True
                break

            # for each neighbor node (including diagonals)
            for nei in self.nodeNeighbors(node, True):
                neiX, neiY = nei

                # if its a wall or marked closed, don't do anything
                if nei in closed or self.matrix[neiX][neiY].c == yellow:
                    continue

                # calculate cost from node to neighbor
                newCost = self.matrix[i][j].g + self.calcCost(node, nei)
                curCost = self.matrix[neiX][neiY].g

                # continue if not visited or new cost is less then the current cost
                if curCost == sys.maxsize or newCost < curCost:
                    # update and recalculate h and f
                    self.matrix[neiX][neiY].g = newCost
                    h = self.heuristic(nei, self.end)
                    f = newCost + h

                    # set parent and add to the queue
                    heapq.heappush(priorityQueue, (f, nei))
                    self.matrix[neiX][neiY].parent = node
                    self.colorQ.put((neiX, neiY, green))
        self.backtrack()

    # returns one if in same row/column, else 1.414
    def calcCost(self, me, node):
        if abs(me[0] - node[0]) + (me[1] - node[1]) == 1:
            return 1
        else:
            return 1.414

    def heuristic(self, node, end):
        diag = 1.414
        deltaX = abs(node[0] - end[0])
        deltaY = abs(node[1] - end[1])
        return min(deltaX, deltaY) * diag + abs(deltaX - deltaY)

    def breadthFirstSearch(self):
        # make each node parent itself
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y].parent = (x, y)

        # a queue to store nodes to check / travel to next
        myQueue = queue.Queue()
        myQueue.put(self.start)

        # set start node to cost 0
        self.matrix[self.start[0]][self.start[1]].g = 0

        # for every node in queue
        while not myQueue.empty():
            node = myQueue.get()

            # if at end node, stop
            if node == self.end:
                break

            # for each neighbor node
            for nei in self.nodeNeighbors(node, False):
                neiX, neiY = nei

                # if its a wall, don't do anything
                if self.matrix[neiX][neiY].c == yellow:
                    continue

                # only set parent if node has not already been visited
                if self.matrix[neiX][neiY].c == black:
                    myQueue.put(nei)
                    self.colourMatrix(neiX, neiY, green)
                    self.matrix[neiX][neiY].parent = node
                    self.colorQ.put((neiX, neiY, green))
                else:
                    self.colorQ.put((neiX, neiY, red))
        self.backtrack()

    def depthFirstSearch(self):
        # a queue to store nodes to check / travel to next
        myQueue = queue.LifoQueue()
        myQueue.put(self.start)

        # for every node in queue
        while not myQueue.empty() and self.atEndNode == False:
            node = myQueue.get()
            thisX, thisY = node

            # if its a wall, don't do anything
            if self.matrix[thisX][thisY].c == yellow:
                continue

            # make the current node green
            self.colourMatrix(thisX, thisY, green)
            self.colorQ.put((thisX, thisY, green))

            # for each neighbor node
            for nei in self.nodeNeighbors(node, False):
                neiX, neiY = nei

                # only set parent if node has not already been visited
                if self.matrix[neiX][neiY].c == black:
                    self.matrix[neiX][neiY].parent = node
                    myQueue.put((neiX, neiY))

                    # stop if end has been found
                    if (neiX, neiY) == self.end:
                        self.atEndNode = True
                        break
        self.backtrack()

    # find the path the algorithm took
    def backtrack(self):
        cur = self.end
        while cur != self.start:
            # colour in path white (using parent)
            cur = self.matrix[cur[0]][cur[1]].parent
            self.colorQ.put((cur[0], cur[1], white))
        # make start and end node blue
        self.colorQ.put((self.end[0], self.end[1], blue))
        self.colorQ.put((self.start[0], self.start[1], blue))
