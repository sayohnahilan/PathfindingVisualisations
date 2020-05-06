import pygame

class node:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self, window):
        if self.type == "nth":
            pygame.draw.rect(window, [255, 255, 255], (self.x, self.y, 20, 20), 0)