import sys
from colours import *

class Node:
    c = black
    parent = (0, 0)
    g = sys.maxsize  # cost
    h = 0
    f = 0


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
        adj = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        if diag == True:
            adj.extend([(x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)])
        adj = filter(self.onScreen, adj)
        return adj

    # check if neighbor nodes are in confinement
    def onScreen(self, node):
        x, y = node
        if 0 <= x < self.x and 0 <= y < self.y:
            return True
        else:
            return False

    # returns one if in same row/column, else 1.414
    def calcCost(self, me, node):
        if abs(me[0] - node[0]) + (me[1] - node[1]) == 1:
            return 1
        else:
            return 1.414

    # cost function from current node to end node
    def heuristic(self, node, end):
        diag = 1.414
        deltaX = abs(node[0] - end[0])
        deltaY = abs(node[1] - end[1])
        return min(deltaX, deltaY) * diag + abs(deltaX - deltaY)
