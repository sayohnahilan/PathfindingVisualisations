import pygame
from nodes import node
from startend import startEnd

pygame.init()

size = [800, 800]
window = pygame.display.set_mode(size)
pygame.display.set_caption('Visualizing A Star Path Finding')

clock = pygame.time.Clock()
fps = 120

start = startEnd(20, 20, "start")
end = startEnd(760, 760, "end")

grid = []
for y in range(0, 800, 20):
    for x in range(0, 800, 20):
        grid.append(node(x, y, "nth"))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    for box in grid:
        box.draw(window)
    start.draw(window)
    end.draw(window)

    pygame.display.update()
    clock.tick(fps)