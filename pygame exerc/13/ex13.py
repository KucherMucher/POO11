import pygame
import sys
import random
import math


pygame.init()


width, height = 1080, 600
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
distance = 0

vel = 0


running = True
while running:
    # Tratar eventos (como fechar a janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        vel-=1
    elif keys[pygame.K_RIGHT]:
        vel+=1
    elif keys[pygame.K_SPACE]:
        if vel > 0:
            vel -= 1
        elif vel < 0:
            vel += 1
            

    pos_x = pos_x+vel

    distance = distance + math.sqrt((vel**2))

    #if (keys[pygame.K_a] == False or keys[pygame.K_d] == False):
        #if v_0 == 0:

    if pos_x + size_carro[0] < 0:
        pos_x = width
    elif pos_x - size_carro[0] > width:
        pos_x = 0 - size_carro[0]


    text = font.render(f"Velocidade atual: {vel} pix/frame", True, (250, 250, 250))
    text2 = font.render(f"Distância percorrida: {distance} pix.", True, (250, 250, 250))
    screen.fill((0, 120, 0))
    pygame.draw.rect(screen, (100, 100, 100), (0, 410, width, 100))
    carro = pygame.draw.rect(screen, beige, ((pos_x, pos_y), size_carro))

    screen.blit(text, (10, 10))
    screen.blit(text2, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()