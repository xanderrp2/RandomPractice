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
clock = pygame.time.Clock()
pop = False
speed = 10
plasment = {}
ballOn = False
place = 999
counter = 1
balloon1 = pygame.image.load("balloon.png")
balloon2 = pygame.tansform.scale(balloon1,(50,200))

class balloon():
    def __init__(self,timeOn,speed,Y):
        self.X = random.randint(50,950)
        self.Y = Y
        self.color = (0,0,255)
        self.size = 50
        self.timeOn = timeOn
        self.speed = speed
    def draw(self):
        scree.blit(balloon2,(self.X,self.Y))

balloon1 = balloon(0,1,950)
balloon2 = balloon(0,random.randint(1,10),950)
balloon3 = balloon(0,random.randint(1,10),950)
balloon4 = balloon(0,random.randint(1,10),950)
balloon5 = balloon(0,random.randint(1,10),950)
balloon6 = balloon(0,random.randint(1,10),950)
balloons = [balloon1,balloon2,balloon3,balloon4,balloon5,balloon6]
while True:
    screen.fill((0,0,0))
    
    balloons[counter].draw()
    balloons[counter].Y = balloons[counter].Y - balloons[counter].speed
    pygame.display.update()
    if counter <= 6:
        counter = 1

    if pop == True:
        counter = counter+1
    
  
    
    


        
    
    

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                pop = True
        
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
