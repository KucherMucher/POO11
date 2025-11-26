import pygame
import sys
import random


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulação do carro")

font = pygame.font.Font(None, 40)

clock = pygame.time.Clock()

#propriedades do carro
size_carro = [70, 40]
beige = (200, 200, 180)

#físicas do carro
pos_x = 400
pos_y = 400

v_0 = 0
v_x = 0
acel = 1
t = 0


running = True
while running:
    # Tratar eventos (como fechar a janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((0, 120, 0))
    pygame.draw.rect(screen, (100, 100, 100), (0, 410, 800, 100))
    carro = pygame.draw.rect(screen, beige, ((pos_x, pos_y), size_carro))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()