import pygame

pygame.init()



red = (255, 0, 0)
blue = (0, 180, 255)
green = (0, 255, 100)

circle_coord = [100, 300]
rect_coord = [10, 10]
rect_size = [50, 50]

black = (0, 0, 0)
white = (255, 255, 255)


s = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    match s:
        case 1:
            screen = pygame.display.set_mode((800, 600))
            for circle in range(10):
                pygame.draw.circle(screen, blue, (circle_coord[0]+circle*60, circle_coord[1]), 30)

        case 2:
            screen = pygame.display.set_mode((800, 600))
            for raw in range(5):
                for culumn in range (6):
                    pygame.draw.rect(screen, green, ((rect_coord[0] + (rect_size[0] + rect_coord[0])*culumn), (rect_coord[1] + (rect_size[0] + rect_coord[1]) * raw ), rect_size[0], rect_size[1]))
        
        case 3:
            screen = pygame.display.set_mode((400, 400))

    pygame.display.update()
    #asdas

    screen.fill((75, 75, 75))

