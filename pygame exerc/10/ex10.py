import pygame
import sys
import math

#init pygame
pygame.init()

#definir dimensões
largura, altura = 600, 400
janela = pygame.display.set_mode((largura, altura))

#definir cores
cor_fundo = (0,0,0) #black
cor_circulo = (255, 0, 0) #red
cor_rect = (0, 0, 255) #blue
cor_circulo2 = (0, 0, 255) #blue


#definir propriedades dos circulos
raio_circus=20

x_circus = raio_circus
y_circus = altura // 2

x_circus2 = raio_circus
y_circus2 = raio_circus


#definir propriedades do quadrado
rect_size = 40
x_rect = raio_circus
y_rect = altura // 2


#definir velocidades
velocidade_rect = 5
velocidade_circus = velocidade_rect/2

velocidade_circus2 =velocidade_circus


#loop principal
while True:
    #verificar os eventos´
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #mover objetos
    x_circus+=velocidade_circus
    y_rect+=velocidade_rect

    dx = largura - x_circus2
    dy = altura - 5 - y_circus2
    angle = math.atan2(dy, dx)
    x_circus2+=velocidade_circus2*math.cos(angle)
    y_circus2+=velocidade_circus2*math.sin(angle)

    #condição das bordas
    if x_circus - raio_circus < 0 or x_circus + raio_circus > largura:
        velocidade_circus = -velocidade_circus
    
    if y_rect < 0 or y_rect + rect_size > altura:
        velocidade_rect = -velocidade_rect

    if x_circus2 - raio_circus < 0 or x_circus2 + raio_circus > largura:
        velocidade_circus2 = -velocidade_circus2
    
    #preencher fundo
    janela.fill(cor_fundo)

    #desenhar objetos
    pygame.draw.circle(janela, cor_circulo, (x_circus, y_circus), raio_circus)
    pygame.draw.rect(janela, cor_rect, (x_rect, y_rect, rect_size, rect_size))
    pygame.draw.circle(janela, cor_circulo2, (x_circus2, y_circus2), raio_circus)

    #autalizar o display
    pygame.display.flip()

    #fps
    pygame.time.Clock().tick(60)