import pygame

pygame.init()

CELL_SIZE = 30
SCREEN_WIDTH = 15 * CELL_SIZE
SCREEN_HEIGHT = 20 * CELL_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris v 0.1')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()



pygame.quit()