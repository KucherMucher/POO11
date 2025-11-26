import pygame
import sys

pygame.init()



fonte = pygame.font.Font(None, 30)

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((600, 600))

rect_size=50
rect_coord=[100, 100]
running = True
cor = True
letra  = 65

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((120, 120, 120))
    for raw in range(8):
        cor = (raw%2 == 0)
        for culumn in range(8):
            color = white if cor else black
            pygame.draw.rect(screen, color, (rect_coord[0]+(rect_size*culumn), rect_coord[1]+(rect_size*raw), rect_size, rect_size))
            
            screen.blit(fonte.render(f"{chr(65+culumn)}", True, (0, 0, 0)), (rect_coord[0]+ 17+ rect_size*culumn, rect_coord[1]-rect_size/2))
            screen.blit(fonte.render(f"{chr(65+culumn)}", True, (0, 0, 0)), (rect_coord[0]+17+ rect_size*culumn, rect_coord[1]+rect_size*8+10))
            screen.blit(fonte.render(f"{1+raw}", True, (0, 0, 0)), (rect_coord[0]-rect_size/2, rect_coord[0]+14+rect_size*raw)) #é assim as coordenadas dos textos para fazer
            screen.blit(fonte.render(f"{1+raw}", True, (0, 0, 0)), (rect_coord[0]+rect_size*8+10, rect_coord[0]+14+rect_size*raw))

            cor = not cor

    pygame.display.update()

pygame.quit()
sys.exit()




texto = fonte.render(f"Tempo deste início: {str(round(tempo, 3))}", True, (0, 0, 0))
ecra.blit(texto2, (10, 50))
