import pygame

pygame.init()



red = (255, 0, 0)
blue = (0, 180, 255)
green = (0, 255, 100)
grey = (75, 75, 75)

black = (0, 0, 0)
white = (255, 255, 255)



s = 1 #tem que mudar esse númerto para ver os exercícios

match s:
    case 1: #ex 1
        screen = pygame.display.set_mode((800, 600))

        circle_coord = [100, 300]

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen.fill(grey)
            for circle in range(10):
                pygame.draw.circle(screen, blue, (circle_coord[0]+circle*60, circle_coord[1]), 30)
            pygame.display.update()





    case 2: #ex 2
        screen = pygame.display.set_mode((800, 600))

        rect_coord = [10, 10]
        rect_size = [50, 50]
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen.fill(grey)
            for raw in range(5):
                for culumn in range (6):
                    pygame.draw.rect(screen, green, ((rect_coord[0] + (rect_size[0] + rect_coord[0])*culumn), (rect_coord[1] + (rect_size[0] + rect_coord[1]) * raw ), rect_size[0], rect_size[1]))
            pygame.display.update()






    case 3: #ex 3
        screen = pygame.display.set_mode((400, 400))

        rect_size=50
        rect_coord=[0, 0]
        running = True
        cor = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for raw in range(8):
                cor = (raw%2 == 0)
                for culumn in range(8):
                    color = white if cor else black
                    pygame.draw.rect(screen, color, (rect_coord[0]+(rect_size*culumn), rect_coord[1]+(rect_size*raw), rect_size, rect_size))
                
                    cor = not cor

            pygame.display.update()

    
    case 4:
        screen = pygame.display.set_mode((800, 600))

        diameter = 20
        circle_coord = [100, 100]
        yellow = (255, 255, 0)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for stair in range(10):
                pygame.draw.circle(screen, yellow, (circle_coord[0]+(30*stair), circle_coord[1]+(30*stair)), diameter)
            

            pygame.display.update()

            

    #asdas

    

