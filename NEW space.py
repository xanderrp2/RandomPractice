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
import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def WiN(msg,x,y):
    fontobj = pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg,False,(255,255,0))
    screen.blit(msgobj,(x,y))



class Charac():
    def __init__(self,image,x,y,width,height):
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height

    def image(self):
        charac = pygame.image.load("alien.png")
        charac = pygame.transform.scale(alien1,(self.width,self.height))
    def showimage(self):
        screen.blit(self.image,(self.x,self.y))
        


class alien(Charac):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
 
    def MOVE(self):
        self.x = self.x + self.change
        self.times = self.times +1

A = alien(pygame.transform.scale(pygame.image.load("alien.png"),10,10))



while True:
    A.draw()






    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
