from menu_file import *
import pygame
import random
from pygame.locals import *
from snake.py import *
from flappy_bird.py import *
from pong.py import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def WiN(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans",100)
    msgobj = fontobj.render(msg,False,(color))
    screen.blit(msgobj,(x,y))
while True:
    pygame.draw.rect(screen,(0,255,0),(250,350,500,200),5)
    pygame.draw.rect(screen,(0,255,0),(250,650,500,200),5)
    WiN("Play",400,400,(0,0,255))
    WiN("Quit",400,700,(255,0,0))
    pygame.display.update()







    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("first")
            (x,y) = event.pos
            if 200 < x < 800 and 300 < y < 500:
                screen.fill((0,0,0))
                SnAkE()
                pygame.display.update()
            if 200 < x < 800 and 600 < y < 800:
                screen.fill((0,0,0))
                pygame.quit()
                exit()
                pygame.display.update()
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
