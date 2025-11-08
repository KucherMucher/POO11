import pygame # pyright: ignore[reportMissingImports]

pygame.init()

screen = pygame.display.set_mode((900, 900))

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)



p1 = [200, 200]
p2 = [200, 700]
p3 = [700, 200]
p4 = [700, 700]

p5 = [300, 300]
p6 = [300, 600]
p7 = [600, 300]
p8 = [600, 600]



border = (0, 900)




fps = pygame.time.Clock()

line1 = [p1, p2]
line2 = [p5, p6]
line3 = [p7, p8]
line4 = [p3, p4]

p1ph=[p1[0], p1[1]]  # Create new lists with copied values
p2ph=[p2[0], p2[1]]
p3ph=[p3[0], p3[1]]
p4ph=[p4[0], p4[1]]
p5ph=[p5[0], p5[1]]
p6ph=[p6[0], p6[1]]
p7ph=[p7[0], p7[1]]
p8ph=[p8[0], p8[1]]

#x


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.line(screen, red, line1[0], line1[1], 2)
    pygame.draw.line(screen, red, p1, p3, 2)
    pygame.draw.line(screen, red, p2, p4, 2)
    pygame.draw.line(screen, blue, line4[0], line4[1], 2)

    pygame.draw.line(screen, red, p1, p4, 2)
    pygame.draw.line(screen, red, p2, p3, 2)

    pygame.draw.line(screen, green, line2[0], line2[1], 2)
    pygame.draw.line(screen, red, p5, p7, 2)
    pygame.draw.line(screen, red, p6, p8, 2)
    pygame.draw.line(screen, yellow, line3[0], line3[1], 2)


    pygame.draw.line(screen, red, p1, p5, 2)
    pygame.draw.line(screen, red, p2, p6, 2)
    pygame.draw.line(screen, red, p3, p7, 2)
    pygame.draw.line(screen, red, p4, p8, 2)
    
    

    
    if int(p1[0])==p1ph[0] and int(p1[1])==p1ph[1]:
        transform_fase = 1
    elif int(p1[0])==p5ph[0] and int(p1[1])==p5ph[1]:
        transform_fase = 2
    elif int(p1[0])==p7ph[0] and int(p1[1])==p7ph[1]:
        transform_fase = 3
    elif int(p1[0])==p3ph[0] and int(p1[1])==p3ph[1]:
        transform_fase = 4
    
    match transform_fase:
        case 1:
            #transform p1 -> p5
            p1[0]+=10
            p1[1]+=10

            #trasnform p2 -> p6
            p2[0]+=10
            p2[1]-=10

            #transform p5 -> p7
            p5[0]+=30
            
            #trasnform p6 -> p8
            p6[0]+=30

            #trasnform p7 -> p3
            p7[0]+=10
            p7[1]-=10

            #trasnform p8 -> p4
            p8[0]+=10
            p8[1]+=10

            #transform p3 -> p1

            p3[0]-=50
            #transform p4 -> p2
            p4[0]-=50


        case 2:

            #transform p3 -> p1
            p3[0]+=10
            p3[1]+=10

            #transform p4 -> p2
            p4[0]+=10
            p4[1]-=10

            #transform p1 -> p5
            p1[0]+=30
            
            #trasnform p2 -> p6
            p2[0]+=30

            #transform p5 -> p7
            p5[0]+=10
            p5[1]-=10

            #trasnform p6 -> p8
            p6[0]+=10
            p6[1]+=10

            #trasnform p7 -> p3
            p7[0]-=50

            #trasnform p8 -> p4
            p8[0]-=50

        case 3:

            #trasnform p7 -> p3
            p7[0]+=10
            p7[1]+=10

            #trasnform p8 -> p4
            p8[0]+=10
            p8[1]-=10

            #transform p3 -> p1
            p3[0]+=30
            
            #transform p4 -> p2
            p4[0]+=30

            #transform p1 -> p5
            p1[0]+=10
            p1[1]-=10

            #trasnform p2 -> p6
            p2[0]+=10
            p2[1]+=10

            #transform p5 -> p7
            p5[0]-=50

            #trasnform p6 -> p8
            p6[0]-=50

        case 4:

            #transform p5 -> p7 
            p5[0]+=10
            p5[1]+=10

            #trasnform p6 -> p8 
            p6[0]+=10
            p6[1]-=10

            #trasnform p7 -> p3
            p7[0]+=30
            
            #trasnform p8 -> p4
            p8[0]+=30

            #transform p3 -> p1 
            p3[0]+=10
            p3[1]-=10

            #transform p4 -> p2
            p4[0]+=10
            p4[1]+=10

            #transform p1 -> p5 
            p1[0]-=50

            #trasnform p2 -> p6
            p2[0]-=50
    

    line1 = [p1, p2, red]
    line2 = [p5, p6, green]
    line3 = [p7, p8, yellow]
    line4 = [p3, p4, blue]
    pygame.display.update()
    fps.tick(24)

    

    #rotate_x(p1, p2, p3, p4, p5, p6, p7, p8)
    screen.fill((0,0,0))
        


    
