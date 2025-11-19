
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
square_color = (0, 0, 255)
square_x, square_y = 375, 275
square_speed = 5
square_size = 50

while True:
    keys = pygame.key.get_pressed()

    # Movimenta o quadrado com as teclas de direção
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed

    # Eventos principais
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a tela
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
