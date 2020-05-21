import queue
from colours import *
from SearchAlgorithms.backTrack import backtrack

def depthFirst(self):
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
    if self.atEndNode:
        backtrack(self)
