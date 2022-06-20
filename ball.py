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

class ball():
    def __init__(self):
        self.X = random.randint(0,1000)
        self.Y = random.randint(0,1000)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.size = random.randint(0,200)
        self.space = False
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.X,self.Y),self.size)
    def isclicked(self,mouse_pos):
        if self.x<mouse_pos[0]<self.x+self.size() and self.y<mouse_pos[1]<self.y+self.size():
            print("ball was clicked")
            ballclicked = True
        else:
            ballclicked = False
    def clicked():
        if ballclicked == True:
            print("")
        
        
v = 0
ball1 = ball()     
balls = [ball1]    
        

while True:
    ball4 = ball()
    if balls[v].space == True:
        balls.append(ball4)
        print(balls)        
        
    for v in range(0,len(balls),1):

        balls[v].draw()
    







    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                balls[v].space = True
            else:
                balls[v].space = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("you have clicked the left mouse button at ", event.pos)
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
