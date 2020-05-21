import pygame

class Board:
    def __init__(self, w, h, c):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(c)

    def drawLines(self, c):
        x = 0
        y = 0
        w = self.width // 20
        for l in range(w):
            pygame.draw.aaline(self.screen, c, (0, y), (self.width, y))
            pygame.draw.aaline(self.screen, c, (x, 0), (x, self.height))
            x += 20
            y += 20

    def colourOne(self, x, y, c):
        x *= 20
        y *= 20
        square = pygame.Rect(y, x, 19, 19)
        pygame.draw.rect(self.screen, c, square)

    def findSquare(self, x, y):
        x = x - (x % 20)
        y = y - (y % 20)
        coord = (x, y)
        return coord