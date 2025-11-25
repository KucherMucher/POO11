import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensoes da janela
largura_janela, altura_janela = 600, 400
ecra = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Controlo do Circulo")

#texto
fonte = pygame.font.Font(None, 40)
tempo = 0
nsaltos = 0

# Configuracoes iniciais do circulo
pos_x_circulo, pos_y_circulo = largura_janela // 2, altura_janela - 30
raio_circulo = 30
velocidade_circulo = 5
cor_circulo = (0, 0, 255)  # Azul inicial

# Fisica do salto
pos_y_inicial = pos_y_circulo        # "chao" do circulo
gravidade = 1                        # aceleracao (pixels/frame^2)
v0_base = -20                        # velocidade inicial base (para cima = negativa)
v0_atual = 0                         # velocidade inicial usada em cada salto
t = 0                                # tempo desde o inicio do salto (em frames)
saltando = False                     # indica se o circulo esta a saltar
energia = 1.0                        # fator de energia (100% no inicio)

relogio = pygame.time.Clock()

executar = True
while executar:
    # Tratar eventos (como fechar a janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executar = False

    teclas = pygame.key.get_pressed()

    #texto
    texto = fonte.render(f"Tempo deste início: {str(round(tempo, 3))}", True, (0, 0, 0))
    tempo += 1/60

    texto2 = fonte.render(f"Número de saltos: {str(round(nsaltos, 0))}", True, (0,0,0))
    

    # Movimento do circulo (apenas para a esquerda e direita)
    if teclas[pygame.K_LEFT]:
        pos_x_circulo -= velocidade_circulo
    if teclas[pygame.K_RIGHT]:
        pos_x_circulo += velocidade_circulo

    # Saltar com a tecla UP (apenas se estiver no chao / nao estiver a saltar)
    if teclas[pygame.K_UP] and saltando == False:
        saltando = True
        t = 0
        energia = 1.0           # volta a ter energia total quando carregas UP
        v0_atual = v0_base * energia

    # Atualizar a posicao vertical usando a lei do movimento:
    # y = y0 + v0 * t + 1/2 * a * t^2
    if saltando:
        t += 1  # contamos o tempo em "frames"
        pos_y_circulo = pos_y_inicial + v0_atual * t + 0.5 * gravidade * t * t

        # Se chegar ao chao (posicao inicial), nao passa para baixo:
        if pos_y_circulo >= pos_y_inicial:
            pos_y_circulo = pos_y_inicial
            t = 0

            nsaltos+=1

            # perde 10% da energia em cada salto
            energia *= 0.9
            v0_atual = v0_base * energia

            # se a energia for muito pequena, paramos o salto
            if abs(v0_atual) < 2:
                saltando = False

    # Mudar a cor com a barra de espaco
    if teclas[pygame.K_SPACE]:
        cor_circulo = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    # Limites da janela para o eixo x (para evitar que o circulo saia da tela)
    if pos_x_circulo - raio_circulo < 0:
        pos_x_circulo = raio_circulo
    if pos_x_circulo + raio_circulo > largura_janela:
        pos_x_circulo = largura_janela - raio_circulo

    # Atualizar e desenhar
    ecra.fill((255, 255, 255))
    pygame.draw.circle(ecra, cor_circulo, (pos_x_circulo, int(pos_y_circulo)), raio_circulo)
    ecra.blit(texto, (10, 10))
    ecra.blit(texto2, (10, 50))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
