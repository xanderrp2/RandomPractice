import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")

while True:
    mouseX = random.randint(0,1000)
    mouseY = random.randint(0,1000)
##    pygame.draw.circle(screen,(0,255,0),(100,100),100,2)
##    pygame.draw.rect(screen,(0,255,0),(50,50,150,150),5)
##    pygame.draw.rect(screen,(0,255,0),(0,0,50,50),5)
##    pygame.draw.rect(screen,(0,255,0),(850,850,50,50),5)
##    pygame.draw.circle(screen,(0,255,0),(0,0),100,2)
##    pygame.draw.circle(screen,(0,255,0),(0,1000),100,2)
##    pygame.draw.circle(screen,(0,255,0),(1000,0),100,2)
##    pygame.draw.circle(screen,(0,255,0),(1000,1000),100,2)
##    pygame.draw.circle(screen,(0,255,0),(500,500),100,2)
##    pygame.draw.line(screen,(0,255,0),(50,50),(50,950),2)
##    pygame.draw.line(screen,(0,255,0),(50,50),(950,950),2)
##    pygame.draw.line(screen,(0,255,0),(50,950),(950,950),2)
##    pygame.draw.polygon(screen,(0,255,0),((50,50),(950,950),(50,950),(700,700),(750,750)),5)
    for i in range(0,1000,100):
        pygame.draw.line(screen,(0,255,0),(0,i),(1000,i),2)
    for i in range(0,1000,100):
        pygame.draw.line(screen,(0,255,0),(i,0),(i,1000),2)
    
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (x,y) = event.pos
            if 1000 > x > 0 and 1000 > y > 0:
                pygame.draw.circle(screen,(0,255,0),(mouseX,mouseY),100,2)
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    
    
