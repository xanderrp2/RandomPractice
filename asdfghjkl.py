import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def WiN(msg,x,y):
    fontobj = pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg  ,False,(255,255,0))
    screen.blit(msgobj,(x,y))
points = 0
boom = 200
x = 12
bullet = -25
bullet1 = 50
bom = 25
change = 25
Fire = False
sprite = pygame.image.load("greenCar.png")
sprite1 = pygame.transform.scale(sprite,(25,100))
alien = pygame.image.load("bird_wingsUp.png")
alien1 = pygame.transform.scale(alien,(200,200))


while True:
    screen.fill((0,0,0))
    if Fire == True:
        print("1")
        for i in range(0,40,1):
            pygame.draw.circle(screen,(25,255,25),(x,bullet1),(50))
            bullet1 = bullet1 + bullet
    if bullet1 <= 0:
        print("2")
        Fire = False
        bullet1 = 950
        
    if 600>x>400 and Fire == True: 
        print("3")
        print("you win")
    if points == 5 or points == 10 or points == 15:

        pygame.draw.circle(screen,(200,23,192),(450,boom),(50))
        boom = boom + 5
    else:
        boom = 200
    if boom == 900:
        WiN("Game Over",450,450)
        pygame.display.update()
        pygame.quit()
        exit()
    
        

        
        
    
    screen.blit(sprite1,(x,900))
    screen.blit(alien1,(400,0))
    x = x + change
    if x >= 975:
        change = -25
    if x <= 25:
        change = 25


    








    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                Fire = True
        if event.type == QUIT:
            pygame.quit()
            exit()
    if 600>x>400 and Fire == True: 
        print("3")
        print("you win")
        points = points + 1
    WiN(str(points),0,0)

    pygame.display.update()

