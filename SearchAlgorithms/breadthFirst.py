import queue
from colours import *
from SearchAlgorithms.backTrack import backtrack

def breadthFirst(self):
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
            self.atEndNode = True
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
    if self.atEndNode:
        backtrack(self)
