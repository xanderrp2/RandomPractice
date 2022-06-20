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
clock = pygame.time.Clock()
birdX = 250
birdY = 500
rectX = 750
rectY = 0
rectlen = random.randint(0,750)
rectlenW = 150
space = 400
score = 0
bounce = False
pipe1up = pygame.image.load("pipeup.png")
pipeup = pygame.transform.scale(pipe1up,(150,rectlen))
pipe1down = pygame.image.load("pipedown 2.png")
pipedown = pygame.transform.scale(pipe1down,(500,rectlen+500))
bird1 = pygame.image.load("bird_wingsUp.png")
bird2 = pygame.image.load("bird_wingsDown.png")
bird1 = pygame.transform.scale(bird1,(100,100))
bird2 = pygame.transform.scale(bird2,(100,100))
background = pygame.image.load("Flappy_bird_Background.png")
bird = bird1
pick = screen.blit(bird1,(birdX,birdY))
prick = screen.blit(bird2,(birdX,birdY))
bird = pick
background1 = pygame.transform.scale(background,(1000,1000))
screen.blit(background1, (0,0))

while True:
    clock.tick(100)
    if bird == bird1:
        bird = pick
        bird = bird2

        
    else:
        bird = prick
        bird = bird1


    screen.blit(background1, (0,0))
  
    screen.blit(pipe1up,(rectX,rectY-960+rectlen))
    screen.blit(pipe1down,(rectX,rectY+rectlen+space,rectlenW,rectlen+800))

    screen.blit(bird,(birdX - 50,birdY - 50))
    pygame.display.update()
    if bounce == True:
        birdY = birdY - 10
    elif bounce == False:
        birdY = birdY + 10
 ##   pygame.draw.rect(screen,(0,255,0),(rectX,rectY,rectlenW,rectlen))
  ##  pygame.draw.rect(screen,(0,255,0),(rectX,rectY+rectlen+space,rectlenW,rectlen+800))
    rectX = rectX - 10
    WiN("score  " +str(score),400,50)

    pygame.display.update()
    if rectX <= -150:
        rectX = 1000
        rectlen = random.randint(0,750)
    if birdY+50 == 1000:
        WiN("gameover",400,450)
        pygame.display.update()
        break
        exit()
    clock.tick(100)
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
    screen.fill((0,0,0))
    pygame.display.update()
    ##or ( rectY+space+< birdX+50 < 1000 and rectY < birdY < rectY+rectlen)

