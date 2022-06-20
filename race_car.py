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
carX = 100
carY = 100
##carX1
##carY1
##carX2
##carY2


while True:
    pygame.draw.rect(screen,(0,0,255),(carX,carY,100,300))







    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == pygame.K_UP and Sdown == False:
                print("test")

            if event.key == pygame.K_RIGHT and Sleft == False:
                 print("test")

            if event.key == pygame.K_LEFT and Sright == False:
                 print("test")
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
