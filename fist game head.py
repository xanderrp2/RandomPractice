import pygame
import random
##from LSP import *
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def WiN(msg,x,y):
    fontobj = pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg,False,(255,255,0))
    screen.blit(msgobj,(x,y))
## memorisation game
Red = False
Blue = False
Green = False
Yellow = False
RED = False
BLUE = False
GREEN = False
YELLOW =False
pressed = [] ## find out what they pressed in order
random = [] ## make the order random


while True:
    pygame.draw.rect(screen,(255,0,0),(0,0,500,500))
    pygame.draw.rect(screen,(0,255,0),(0,500,500,500))
    pygame.draw.rect(screen,(0,0,255),(500,0,500,500))
    pygame.draw.rect(screen,(150,150,0),(500,500,500,500))
    







    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
