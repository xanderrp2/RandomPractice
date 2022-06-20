from menu_file import *
import pygame
import random
from pygame.locals import *
from snake import *
from BIRDOFTHEFLAP import *
from pong import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def allBUTTONS():
    def WiN(msg,x,y,color):
        fontobj = pygame.font.SysFont("freesans",100)
        msgobj = fontobj.render(msg,False,(color))
        screen.blit(msgobj,(x,y))
    while True:
        pygame.draw.rect(screen,(0,255,0),(250,150,500,200),5)
        pygame.draw.rect(screen,(0,255,0),(250,350,500,200),5)
        pygame.draw.rect(screen,(0,255,0),(250,550,500,200),5)
        pygame.draw.rect(screen,(0,255,0),(250,750,500,200),5)
        WiN("tick tack toe",350,200,(0,0,255))
        WiN("flappy bird",350,400,(255,0,0))
        WiN("snake",400,600,(0,0,255))
        WiN("pong",400,800,(255,0,0))
        pygame.display.update()







        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("first")
                (x,y) = event.pos

                if 200 < x < 800 and 150 < y < 350:
                    screen.fill((0,0,0))
                    GaMe()
                    pygame.display.update()
                if 200 < x < 800 and 350 < y < 550:
                    screen.fill((0,0,0))
                    flappy_bird()
                    pygame.display.update()
                if 200 < x < 800 and 550 < y < 750:
                    screen.fill((0,0,0))
                    snake()
                    pygame.display.update()
                if 200 < x < 800 and 750 < y < 950:
                    pong()
                    pygame.display.update()
                
                    
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
allBUTTONS()
