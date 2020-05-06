import pygame

class startEnd:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self, window):
        if self.type == "start":
            pygame.draw.circle(window, [0, 200, 0], (self.x + 10, self.y + 10), 10)
        if self.type == "end":
            pygame.draw.circle(window, [200, 0, 0], (self.x + 10, self.y + 10), 10)
