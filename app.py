import pygame
from nodes import Node

pygame.init()

size = [700, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Visualizing A Star Path Finding')

clock = pygame.time.Clock()
fps = 120

grid = []
for i in range(0, 700, 20):
    for j in range(0, 700, 20):
        grid.append(Node(j, i))

running = False

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    for box in grid:
        box.draw(screen)