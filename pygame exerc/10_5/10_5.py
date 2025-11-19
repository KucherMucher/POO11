import pygame

pygame.init()

# Configuração da janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Leitura de Teclado")

# Define cores
WHITE = (255, 255, 255)

# Controla o loop principal
running = True

# Relógio para controlar FPS
clock = pygame.time.Clock()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"Tecla pressionada: {pygame.key.name(event.key)}")
        elif event.type == pygame.KEYUP:
            print(f"Tecla solta: {pygame.key.name(event.key)}")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:  # Verifica se a tecla 'Seta para cima' está pressionada
        print("Seta para cima pressionada!")
    if keys[pygame.K_LEFT]:
        print("Seta para esquerda pressionada!")

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
