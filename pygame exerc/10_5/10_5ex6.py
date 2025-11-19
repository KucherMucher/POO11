import pygame
import sys
import math
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
largura, altura = 600, 400
screen = pygame.display.set_mode((largura, altura))
# Configurações iniciais

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

circle_color = blue

circle_x, circle_y = 375, 275
circle_speed = 5
circle_size = 50


colorList=[red, blue, green]

while True:
    keys = pygame.key.get_pressed()

    # Movimenta o quadrado com as teclas de direção
    if keys[pygame.K_UP]:
        if circle_y-circle_size != 0:
            circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        if circle_y+circle_size != altura:
            circle_y += circle_speed
    if keys[pygame.K_LEFT]:
        if circle_x-circle_size != 0:
            circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        if circle_x+circle_size != largura:
            circle_x += circle_speed
    if keys[pygame.K_SPACE]:
        circle_color = random.choice(colorList)
    if keys[pygame.K_ESCAPE]:
        pygame.event = pygame.QUIT
        sys.exit()

    # Eventos principais
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a tela
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_size)
    pygame.display.flip()
    pygame.time.Clock().tick(60)