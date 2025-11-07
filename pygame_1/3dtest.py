import pygame

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

line1 = [p1, p2, red]
line2 = [p5, p6, green]
line3 = [p7, p8, yellow]
line4 = [p3, p4, blue]

border = (0, 900)

direction = "left" #/"right"
density = "outside" #/"inside"

fps= pygame.time.Clock()

#x
"""
def rotate(p1, p2, p3, p4, p5, p6, p7, p8):
    global direction
     #True - left, false - right

    if direction=="left":
        if p3[0]==0:
            direction="right"
        else:
            goLeft_x(p1, p2, p3, p4, p5, p6, p7, p8)
            print(direction)

    elif direction=="right":
        if p1[0]==900:
            direction="left"
        else:
            goRight_x(p1, p2, p3, p4, p5, p6, p7, p8)
            print(direction)

def goLeft_x(p1, p2, p3, p4, p5, p6, p7, p8):
    print(p3)
    p1[0]-=10
    p2[0]-=10
    p3[0]-=10
    p4[0]-=10

    p5[0]+=10
    p6[0]+=10
    p7[0]+=10
    p8[0]+=10

def goRight_x(p1, p2, p3, p4, p5, p6, p7, p8):
    print(p1)
    p1[0]+=10
    p2[0]+=10
    p3[0]+=10
    p4[0]+=10

    p5[0]-=10
    p6[0]-=10
    p7[0]-=10
    p8[0]-=10

#y

def submerge(p1, p2, p3, p4, p5, p6, p7, p8):
    print("submerged left")

#ideia - change positions of each line (make each line a variable), and then add transitions. for example:
# line 1 - xy
# line 2 - -x-y
# line 3 - -2x-2y
# line 4 - -2x-2y
#sadsad
"""

def change_pos_x(line1, line2, line3, line4):
    global direction

    if direction=="left":
        line1ph = line1[0]
        line2ph = line2[0]
        line3ph = line3[0]
        line4ph = line4[0]

        line1[0] = line2ph[0]
        line2[0] = line3ph[0]
        line3[0] = line4ph[0]
        line4[0] = line1ph[0]

        line1ph[1] = line1[1]
        line2ph[1] = line2[1]
        line3ph[1] = line3[1]
        line4ph[1] = line4[1]

        line1 = line2ph[1]
        line2 = line3ph[1]
        line3 = line4ph[1]
        line4 = line1ph[1]

        print(direction)

    elif direction=="right":
        if p1[0]==900:
            direction="left"
        else:
            print(direction)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.line(screen, line1[2], line1[0], line1[1], 2)
    #pygame.draw.line(screen, red, p1, p3, 2)
    #pygame.draw.line(screen, red, p2, p4, 2)
    pygame.draw.line(screen, line4[2], line4[0], line4[1], 2)

    #pygame.draw.line(screen, red, p1, p4, 2)
    #pygame.draw.line(screen, red, p2, p3, 2)

    pygame.draw.line(screen, line2[2], line2[0], line2[1], 2)
    #pygame.draw.line(screen, red, p5, p7, 2)
    #pygame.draw.line(screen, red, p6, p8, 2)
    pygame.draw.line(screen, line3[2], line3[0], line3[1], 2)


    #pygame.draw.line(screen, red, p1, p5, 2)
    #pygame.draw.line(screen, red, p2, p6, 2)
    #pygame.draw.line(screen, red, p3, p7, 2)
    #pygame.draw.line(screen, red, p4, p8, 2)

    pygame.display.update()
    fps.tick(8)

    change_pos_x(line1, line2, line3, line4)

    #rotate_x(p1, p2, p3, p4, p5, p6, p7, p8)
    screen.fill((0,0,0))
        


    
