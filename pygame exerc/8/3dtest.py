import pygame

pygame.init()

screen = pygame.display.set_mode((900, 900))

red = (255, 0, 0)

p1 = [200, 200]
p2 = [200, 700]
p3 = [700, 200]
p4 = [700, 700]

p5 = [300, 300]
p6 = [300, 600]
p7 = [600, 300]
p8 = [600, 600]

border = (0, 900)

direction = "left"

fps= pygame.time.Clock()

def rotate(p1, p2, p3, p4, p5, p6, p7, p8):
    global direction
     #True - left, false - right

    if direction=="left":
        if p3[0]==0:
            direction="right"
        else:
            goLeft(p1, p2, p3, p4, p5, p6, p7, p8)
            print(direction)

    elif direction=="right":
        if p1[0]==900:
            direction="left"
        else:
            goRight(p1, p2, p3, p4, p5, p6, p7, p8)
            print(direction)
#asdasasd
    


def goLeft(p1, p2, p3, p4, p5, p6, p7, p8):
    print(p3)
    p1[0]-=10
    p2[0]-=10
    p3[0]-=10
    p4[0]-=10

    p5[0]+=10
    p6[0]+=10
    p7[0]+=10
    p8[0]+=10

def goRight(p1, p2, p3, p4, p5, p6, p7, p8):
    print(p1)
    p1[0]+=10
    p2[0]+=10
    p3[0]+=10
    p4[0]+=10

    p5[0]-=10
    p6[0]-=10
    p7[0]-=10
    p8[0]-=10


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.line(screen, red, p1, p2, 2)
    pygame.draw.line(screen, red, p1, p3, 2)
    pygame.draw.line(screen, red, p2, p4, 2)
    pygame.draw.line(screen, red, p3, p4, 2)

    #pygame.draw.line(screen, red, p1, p4, 2)
    #pygame.draw.line(screen, red, p2, p3, 2)

    pygame.draw.line(screen, red, p5, p6, 2)
    pygame.draw.line(screen, red, p5, p7, 2)
    pygame.draw.line(screen, red, p6, p8, 2)
    pygame.draw.line(screen, red, p7, p8, 2)


    pygame.draw.line(screen, red, p1, p5, 2)
    pygame.draw.line(screen, red, p2, p6, 2)
    pygame.draw.line(screen, red, p3, p7, 2)
    pygame.draw.line(screen, red, p4, p8, 2)

    pygame.draw.rect(screen, (0,255,0), (20, 20, 100, 100), 1)
    pygame.draw.circle(screen, (0,255,0), (200, 100), 40, 1)
    pygame.draw.ellipse(screen, (0,255,0), (20, 100, 200, 100), 1)

    pygame.display.update()
    fps.tick(60)

    rotate(p1, p2, p3, p4, p5, p6, p7, p8)
    screen.fill((0,0,20))
        


    
