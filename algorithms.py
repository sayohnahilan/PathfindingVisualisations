class Node:
    c = "B"
    parent = (0, 0)


class Algorithm:
    def __init__(self, x, y, start, end):
        self.x = x
        self.y = y
        self.start = start
        self.end = end
        self.matrix = [[Node() for i in range(x)] for j in range(y)]

    # return nodes to each side of a center node
    def neighbourNodes(self, node):
        x, y = node
        neighbors = [(x, x + 1), (x + 1, x), (x, x - 1), (x - 1, x)]
        neiNodes = filter((0 <= x < self.x and 0 <= y < self.y), neighbors)
        return neiNodes

    