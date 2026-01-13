import sys
import pygame
import random

pygame.init()

width  = 900
height = 900
screen = pygame.display.set_mode((width, height))

grey = (100, 100, 100)

fps = pygame.time.Clock()

tile_coord = [0, 0]
tile_size = width/100
tile_list = []
empty = 0

class Tile:
    def __init__(self, row, column, tile):
        self.r = row
        self.c = column
        self.t = tile

for r in range(100):
    for c in range(100):
        if random.randint(2, 3) == 3:
            tile_list.append(Tile(r, c, "empty"))
            """
            Ideias:
            create lists in a list for columns and rows to easily acess each parameter
            or
            somehow use a class to ffind out the tiles neighbours
            """
            empty += 1
            continue
        else:
            rect = (tile_coord[0]+(tile_size*c), tile_coord[1]+(tile_size*r), tile_size, tile_size)
            tile_list.append(Tile(r, c, rect))
            pygame.draw.rect(screen, grey, rect)

def hello_neighbour():
    for i in range(10000):
        tile = tile_list[i]
        n = 8
        #if tile["r"] == 

def kys():
    for i in range(10000):
        tile = tile_list[i]
        if tile["tile"] != "empty":
            my_neighbour_n = hello_neighbour()

def draw_cave():
    kys()
    for i in range(10000):
        tile = tile_list[i]
        if tile["tile"] != "empty":
            pygame.draw.rect(screen, grey, tile["tile"])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    draw_cave()


    pygame.display.update()


pygame.quit()
sys.exit()