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

ballx = 500
bally = 500
paddley = 400
change = -20
changeY = random.randint(-20,20)
points = 0
up = False
down = False


while True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(950,paddley,10,200))
    pygame.draw.rect(screen,(255,255,255),(50,bally - 100 ,10,200))
    pygame.draw.circle(screen,(0,0,255),(ballx,bally),(30))
    if bally >= 970:
        changeY = changeY -(changeY*2)
    if bally <= 30:
        changeY = changeY -(changeY*2)
    if ballx <= 90:
        change = 20
    if bally > paddley and bally < paddley + 200 and  960 > ballx >= 920 :
        print("2")
        change = -20
    ballx = ballx + change
    bally = bally + changeY
    if paddley >= 800:
        down = False
    if paddley <=0:
        up = False
    if ballx >= 950:
        print("you lose")
        pygame.quit()
        exit()
        
    







    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
                
            else:
                up = False
            if event.key == K_DOWN:
                down = True
            else:
                down = False
        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
                

        if event.type == QUIT:
            pygame.quit()
            exit()
    WiN(str(points),0,0)
    if up == True:
        paddley = paddley - 20
    
    if down == True:
        paddley = paddley + 20
    pygame.display.update()
