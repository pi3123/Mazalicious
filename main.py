import pygame
import Cells
import numpy as np


# Helper Methods
def draw(display):
    for row in range(20):
        for col in range(20):
            pygame.draw.rect(
                screen,
                grid[row][col].getColor(),
                grid[row][col].getRect(row, col),
                0
            )
            pygame.draw.rect(
                screen,
                WHITE,
                grid[row][col].getRect(row, col),
                1
            )
    pygame.display.flip()


def gen(arr):
    for row in range(WIDTH * 2):
        for column in range(WIDTH * 2):
            arr[row, column] = Cells.Tile(1, WIDTH)
    np.save("grid", arr)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 50
HEIGHT = WIDTH
MARGIN = 0
WINDOW_SIZE = [WIDTH*20, WIDTH*20]
clock = pygame.time.Clock()

# Generating the grid
grid = np.load("grid.npy",allow_pickle=True)

for row in range(WIDTH*2):
    for column in range(WIDTH*2):
        grid[row,column] = Cells.Tile(0, WIDTH)
np.save("grid", grid)


# Initializing display
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed Grid")


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    draw(screen)
    pygame.time.delay(60*5)
    gen(grid)
    draw(screen)

    clock.tick(60)
    done = True


