import queue

white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

class Node:
    c = black
    parent = (0, 0)


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

    # return the nodes beside a start node
    def nodeNeighbors(self, node):
        x, y = node
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
            for nei in self.nodeNeighbors(node):
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
            for nei in self.nodeNeighbors(node):
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

    def backtrack(self):
        cur = self.end
        while cur != self.start:
            # retrace steps and colour in path (using parent)
            cur = self.matrix[cur[0]][cur[1]].parent
            self.colorQ.put((cur[0], cur[1], white))
        # make start and end node blue
        self.colorQ.put((self.end[0], self.end[1], blue))
        self.colorQ.put((self.start[0], self.start[1], blue))

