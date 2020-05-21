from colours import *

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
