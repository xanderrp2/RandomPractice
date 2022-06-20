import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def WiN(msg,x,y):
    fontobj = pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg,False,(255,255,0))
    screen.blit(msgobj,(x,y))



while True:
    pygame.draw.line(screen,(255,0,0),(500,250),(250,350),5)
    pygame.draw.line(screen,(255,0,0),(250,350),(250,750),5)
    pygame.draw.line(screen,(255,0,0),(250,750),(750,750),5)
    pygame.draw.line(screen,(255,0,0),(750,750),(750,350),5)
    pygame.draw.line(screen,(255,0,0),(500,250),(750,350),5)

        


    
  
    








    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
