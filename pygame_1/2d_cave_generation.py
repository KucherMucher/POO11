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

ind = 1

class Tile:
    def __init__(self, row, column, tile, empty=False):
        self.r = row
        self.c = column
        self.t = tile
        self.e = empty

def white_noise():
    for r in range(100):
        for c in range(100):
            if random.randint(3, 5) == 3:
                tile_list.append(Tile(r, c, None, True))
                """
                Ideias:
                create lists in a list for columns and rows to easily acess each parameter
                or
                somehow use a class to ffind out the tiles neighbours:
                    cound every neighbour using class
                    find and anihilate tiles using class
                """
                continue
            else:
                tile = (tile_coord[0]+(tile_size*c), tile_coord[1]+(tile_size*r), tile_size, tile_size)
                tile_list.append(Tile(r, c, tile))
                pygame.draw.rect(screen, grey, tile)


def hello_neighbour(current_tile):
    n = 0
    for nr in range(-1, 2):
        for nc in range(-1, 2):
            if nr == 0 and nc == 0:
                continue
            my_dear_neighbour = next((tile for tile in tile_list if tile.r == current_tile.r + nr and tile.c == current_tile.c + nc and not tile.e), None)

            if my_dear_neighbour:
                n+=1
    #print(f"\n{current_tile.r, current_tile.c, n}")
    return n

def ANIHILATE():
    for tile in tile_list:
        if tile.r == 0 or tile.r == 99:
            continue
        elif tile.c == 0 or tile.c == 99:
            continue
        else:
            my_neighbour_n = hello_neighbour(tile)

            if my_neighbour_n < 4:
                tile.t = None
                tile.e = True

def ANIHILATE_loop():
    for i in range(1, 5):
        ANIHILATE()

def CLEANUP():
    for tile in tile_list:
        if (tile.r == 0 or tile.r == 99) and tile.e:
            tile.t = (tile_coord[0]+(tile_size*tile.c), tile_coord[1]+(tile_size*tile.r), tile_size, tile_size)
            tile.e = False
        elif (tile.c == 0 or tile.c == 99) and tile.e:
            tile.t = (tile_coord[0]+(tile_size*tile.c), tile_coord[1]+(tile_size*tile.r), tile_size, tile_size)
            tile.e = False
        else:
            my_neighbour_n = hello_neighbour(tile)

            if my_neighbour_n >= 5 and tile.e == True:
                tile.t = (tile_coord[0]+(tile_size*tile.c), tile_coord[1]+(tile_size*tile.r), tile_size, tile_size)
                tile.e = False
def CLEANUP_2():
    for tile in tile_list:
        my_neighbour_n = hello_neighbour(tile)

        if my_neighbour_n == 8 and tile.e == True:
            tile.t = (tile_coord[0]+(tile_size*tile.c), tile_coord[1]+(tile_size*tile.r), tile_size, tile_size)
            tile.e = False
def generate_cave():
    white_noise()
    ANIHILATE_loop()
    CLEANUP()
    CLEANUP_2()

def draw_cave():
    for tile in tile_list:
        if not tile.e:
            pygame.draw.rect(screen, grey, tile.t)

generate_cave()
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