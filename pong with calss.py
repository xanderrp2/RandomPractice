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

class paddle():
    def __init__(self,color,x,y):
        self.x = x
        self.y = y
        self.color = color
        self.up = False
        self.down = False
    def draw(self):
        pygame.draw.rect(screen,(self.color),(self.x,self.y,10,200))
    def MOVE(self):
        if self.up == True:
            self.y = self.y - 20
        if self.down == True:
            self.y = self.y + 20
        if self.y >= 800:
            self.y = 800
        if self.y <= 0:
            self.y = 0
class ball():
    def __init__(self,colour,x,y,size):
        self.x = x
        self.y = y
        self.colour = colour
        self.change_x = 10
        self.change_y = 10
        self.size = size
        self.points_right = 0
        self.points_left = 0
    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.size)
    def MOVE(self):
        self.x = self.x + self.change_x
        self.y = self.y + self.change_y
        if self.y >= 970 or self.y <= 30:
            self.change_y = -self.change_y
        if self.x >= 970  or self.x <= 30:
            self.change_x = -self.change_x
        if self.x >= 970:
            self.points_left = self.points_left +1
        if self.x <= 30:
            self.points_right = self.points_right +1

            
        

pipe1up = pygame.image.load("pbakcgroundcar.png")
pipeup = pygame.transform.scale(pipe1up,(1000,1000))        
    
cat = paddle((255,255,255),950,400)
dog = paddle((255,255,255),50,400)
mouse = ball((0,0,255),500,500,30)




while True:
    screen.fill((0,0,0))
    screen.blit(pipe1up,(0,0))
    WiN(str(mouse.points_right),950,0)
    WiN(str(mouse.points_left),0,0)
    if mouse.x+30 >= cat.x and (cat.y < mouse.y-30 < cat.y+200 or cat.y < mouse.y+30 < cat.y+200) :
        mouse.change_x = -mouse.change_x
    if mouse.x-30 <= dog.x+10 and (dog.y < mouse.y-30 < dog.y+200 or dog.y < mouse.y-30 < dog.y+200) :
        mouse.change_x = -mouse.change_x
        print("collision")
   
    cat.draw()
    cat.MOVE()
    dog.draw()
    dog.MOVE()
    mouse.draw()
    mouse.MOVE()







    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()           
        if event.type == KEYDOWN:
            if event.key == K_UP:
                cat.up = True
            if event.key == K_DOWN:
                cat.down = True
            if event.key == K_w:
                dog.up = True
            if event.key == K_s:
                dog.down = True
        if event.type == KEYUP:
            if event.key == K_UP:
                cat.up = False
            if event.key == K_DOWN:
                cat.down = False
            if event.key == K_w:
                dog.up = False
            if event.key == K_s:
                dog.down = False



    pygame.display.update()
