import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def WiN(msg,x,y):
    fontobj = pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg,False,(255,0,0))
    screen.blit(msgobj,(x,y))
birdX = 250
birdY = 500
rectX = 750
rectY = 0
rectlen = random.randint(0,750)
rectlenW = 150
space = 400
score = 0
bounce = False

while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),(birdX,birdY),50)
    if bounce == True:
        birdY = birdY - 10
    elif bounce == False:
        birdY = birdY + 10
    pygame.draw.rect(screen,(0,255,0),(rectX,rectY,rectlenW,rectlen))
    pygame.draw.rect(screen,(0,255,0),(rectX,rectY+rectlen+space,rectlenW,rectlen+800))
    rectX = rectX - 10
    WiN("score  " +str(score),400,50)

##    pygame.display.update()
    if rectX == -150:
        rectX = 1000
        rectlen = random.randint(0,750)
    if birdY+50 == 1000:
        WiN("gameover",400,450)
        pygame.display.update()
        break
        exit()

    if (rectX < birdX-50 < rectX+rectlenW and rectY < birdY-50 < rectY+rectlen) or (rectX < birdX+50 < rectX+rectlenW and rectY < birdY-50 < rectY+rectlen):
        WiN("gameover",400,450)
        pygame.display.update()
        break
        exit()
    if (rectX < birdX-50 < rectX+rectlenW and rectY+rectlen+space < birdY+50 < 1000) or (rectX < birdX+50 < rectX+rectlenW and rectY+rectlen+space < birdY+50 < 1000):
        WiN("gameover",400,450)
        pygame.display.update()
        break
        exit()
    if  rectX< birdX+50 < rectX+rectlenW and 0<=birdY<=rectlen:
        WiN("gameover",400,450)
        pygame.display.update()
        break
        exit()
    if  rectX< birdX-50 < rectX+rectlenW and 0<=birdY<=rectlen:
        WiN("gameover",400,450)
        pygame.display.update()
        break
        exit()
    if bounce == True:
        birdY = birdY - 10
    elif bounce == False:
        birdY = birdY + 10
    if birdX-50 == rectX+rectlenW:
        score = score+1








    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                bounce = True
        if event.type == KEYUP:
            if event.key == pygame.K_SPACE:
                bounce = False
                
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
##or ( rectY+space+< birdX+50 < 1000 and rectY < birdY < rectY+rectlen)
