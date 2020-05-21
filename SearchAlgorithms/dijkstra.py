import heapq
import sys
from colours import *
from SearchAlgorithms.backTrack import backtrack

def dijkstra(self):
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
                # update and recalculate f
                self.matrix[neiX][neiY].g = newCost
                f = newCost

                # set parent and add to the queue
                heapq.heappush(priorityQueue, (f, nei))
                self.matrix[neiX][neiY].parent = node
                self.colorQ.put((neiX, neiY, green))
    if self.atEndNode:
        backtrack(self)
