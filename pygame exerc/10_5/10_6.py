import math
import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensoes da janela
largura_janela, altura_janela = 600, 400
ecra = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Controlo do Circulo")

# Configuracoes iniciais do circulo
pos_x_circulo, pos_y_circulo = largura_janela // 2, altura_janela // 2
raio_circulo = 30
cor_circulo = (0, 0, 255)  # Azul inicial

relogio = pygame.time.Clock()

#física
acel = 1
velocidade_circulo = 5
tempo = 0
velocidade_y_inicial = 20
zero = False

executar = True
while executar:
    # Tratar eventos (como fechar a janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executar = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            executar = False

    teclas = pygame.key.get_pressed()

    # Movimento do circulo (apenas para a esquerda e direita)
    if teclas[pygame.K_LEFT]:
        pos_x_circulo -= velocidade_circulo
    if teclas[pygame.K_RIGHT]:
        pos_x_circulo += velocidade_circulo
    if teclas[pygame.K_UP]:
        print(zero)

    while zero == False:
            pos_y_circulo-=velocidade_y_inicial
            velocidade_y_inicial-=1
            if velocidade_y_inicial == 0:
                zero == True

   
    # Mudar a cor com a barra de espaco
    if teclas[pygame.K_SPACE]:
        cor_circulo = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
   
    # Limites da janela para o eixo x (para evitar que o circulo saia da tela)
    if teclas[pygame.K_UP] == False:
        pos_y_inicial = pos_y_circulo
        velocidade_y_inicial = velocidade_circulo + 1
        pos_y_circulo = pos_y_inicial + velocidade_y_inicial*tempo + 0.5 * acel * tempo**2
        tempo = tempo+0.1

    if pos_x_circulo - raio_circulo < 0:
        pos_x_circulo = raio_circulo
    if pos_x_circulo + raio_circulo > largura_janela:
        pos_x_circulo = largura_janela - raio_circulo
    if pos_y_circulo - raio_circulo < 0:
        pos_y_circulo = raio_circulo
    if pos_y_circulo + raio_circulo > altura_janela:
        pos_y_circulo = altura_janela - raio_circulo
        tempo = 0

    # Atualizar e desenhar
    ecra.fill((255, 255, 255))
    pygame.draw.circle(ecra, cor_circulo, (pos_x_circulo, pos_y_circulo), raio_circulo)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
