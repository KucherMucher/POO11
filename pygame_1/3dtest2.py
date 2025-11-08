import pygame # pyright: ignore[reportMissingImports]
import math

pygame.init()

screen = pygame.display.set_mode((900, 900))

fps = pygame.time.Clock()

blue = (0, 0, 255)
red = (255, 0, 0)
ang1=math.pi*2
ang2=math.pi/2
ang3=math.pi
ang4=(3*math.pi)/2
time=0

ellipse_rect_top=pygame.Rect(150, 200, 600, 150)

axt=ellipse_rect_top.width/2
byt=ellipse_rect_top.height/2

cxt=ellipse_rect_top.centerx
cyt=ellipse_rect_top.centery

ellipse_rect_bottom=pygame.Rect(150, 600, 600, 150)

axb=ellipse_rect_bottom.width/2
byb=ellipse_rect_bottom.height/2

cxb=ellipse_rect_bottom.centerx
cyb=ellipse_rect_bottom.centery



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    
    #top

    px1t=axt*math.cos(ang1)+cxt
    py1t=byt*math.sin(ang1)+cyt

    px2t=axt*math.cos(ang2)+cxt
    py2t=byt*math.sin(ang2)+cyt

    px3t=axt*math.cos(ang3)+cxt
    py3t=byt*math.sin(ang3)+cyt

    px4t=axt*math.cos(ang4)+cxt
    py4t=byt*math.sin(ang4)+cyt

    #bottom

    px1b=axb*math.cos(ang1)+cxb
    py1b=byb*math.sin(ang1)+cyb

    px2b=axb*math.cos(ang2)+cxb
    py2b=byb*math.sin(ang2)+cyb

    px3b=axb*math.cos(ang3)+cxb
    py3b=byb*math.sin(ang3)+cyb

    px4b=axb*math.cos(ang4)+cxb
    py4b=byb*math.sin(ang4)+cyb




    screen.fill((0,0,0))

    #drawwing axis

    ellipse = pygame.draw.ellipse(screen, blue, ellipse_rect_top , 2)
    ellipse = pygame.draw.ellipse(screen, blue, ellipse_rect_bottom , 2)

    #drawing points
    point1 = pygame.draw.circle(screen, red, (px1t,py1t), 5)
    point2 = pygame.draw.circle(screen, red, (px2t,py2t), 5)
    point3 = pygame.draw.circle(screen, red, (px3t,py3t), 5)
    point4 = pygame.draw.circle(screen, red, (px4t,py4t), 5)

    point5 = pygame.draw.circle(screen, red, (px1b,py1b), 5)
    point6 = pygame.draw.circle(screen, red, (px2b,py2b), 5)
    point7 = pygame.draw.circle(screen, red, (px3b,py3b), 5)
    point8 = pygame.draw.circle(screen, red, (px4b,py4b), 5)

    #drawing lines

    line1=pygame.draw.line(screen, red, (point1.centerx, point1.centery), (point5.centerx, point5.centery), 2)
    line2=pygame.draw.line(screen, red, (point1.centerx, point1.centery), (point2.centerx, point2.centery), 2)
    line3=pygame.draw.line(screen, red, (point1.centerx, point1.centery), (point4.centerx, point4.centery), 2)

    line4=pygame.draw.line(screen, red, (point3.centerx, point3.centery), (point2.centerx, point2.centery), 2)
    line5=pygame.draw.line(screen, red, (point3.centerx, point3.centery), (point7.centerx, point7.centery), 2)
    line6=pygame.draw.line(screen, red, (point3.centerx, point3.centery), (point4.centerx, point4.centery), 2)

    line7=pygame.draw.line(screen, red, (point4.centerx, point4.centery), (point8.centerx, point8.centery), 2)
    line8=pygame.draw.line(screen, red, (point2.centerx, point2.centery), (point6.centerx, point6.centery), 2)

    line9=pygame.draw.line(screen, red, (point5.centerx, point5.centery), (point6.centerx, point6.centery), 2)
    line10=pygame.draw.line(screen, red, (point5.centerx, point5.centery), (point8.centerx, point8.centery), 2)

    line11=pygame.draw.line(screen, red, (point7.centerx, point7.centery), (point6.centerx, point6.centery), 2)
    line12=pygame.draw.line(screen, red, (point7.centerx, point7.centery), (point8.centerx, point8.centery), 2)

    ang1+=0.1
    ang2+=0.1
    ang3+=0.1
    ang4+=0.1

    pygame.display.update()

    fps.tick(24)

    