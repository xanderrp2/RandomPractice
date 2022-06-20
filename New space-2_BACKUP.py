import pygame
import random
import time
from tkinter import *
from tkinter import messagebox
root = Tk()
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
        

    def showimage(self):
        screen.blit(self.image,(self.x,self.y))
        

class ship(Charac):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.right = False
        self.left = False
        self.health = 3
    def Move(self):
        if self.right == True and self.x <= 950 :
            self.x = self.x + 20
        if self.left == True and self.x >= 0:
            self.x = self.x - 20
    def HIT(self):
        self.health = self.health -1
        

class Bullet(Charac):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.Fal = False
        self.fire = False
    def shot(self):
        if self.fire == True:
            self.y = self.y - 20
class alien(Charac):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.change = 10
        self.count = 2
 
    def MOVE(self):
        self.x = self.x + self.change
        self.count = self.count + 1
        if self.count >= 2:
            self.change = -self.change
        if self.count <= 0:
            self.change = 3
class SupAlien(alien):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.change = 10
        self.health = 3
        self.aq = False
        self.bq = False
        self.cq = False
 
    def MOVE(self):
        self.x = self.x + self.change
        if self.x >= 1000 - self.width or self.x <= 0:
            self.y = self.y + 300
            self.change = -self.change
        
    def HIT(self):
        self.health = self.health - 1


SAL = []


A = SupAlien(pygame.transform.scale(pygame.image.load("alien.png"),(50,50)),100,100,50,50)
SAL.append(A)




    
            
            

times = time.time()
  
M = ship(pygame.transform.scale(pygame.image.load("ship.png"),(50,50)),475,900,50,50)


Fire = False          
a = 10
BL = []
ALD = 10


for i in range(0,9,1):


    if a >= 1000:
        a = 0
ad = False
al = False
stay = False
point = 0
while True:
    times2 = time.time()
    
    
    if times2 - times >= 5:
        A = SupAlien(pygame.transform.scale(pygame.image.load("alien.png"),(50,50)),100,100,50,50)
        SAL.append(A)
        times = time.time()
        print(times)


    screen.fill((0,0,0))
    for i in SAL:
        i.showimage()
        i.MOVE()
    M.showimage()
    M.Move()


    if stay == True:
        for I in BL:
            I.showimage()
            I.fire = True
            I.shot()
            if I.y <= 0:
                BL.remove(I)




    
                
    if stay == True:
        for A in SAL:
            for I in BL:
                if A.x <= I.x <= A.x+100 and A.y <= I.y <= A.y + 100:
                    A.HIT()
                    BL.remove(I)
                    if A.health == 0:
                        SAL.remove(A)
                        point = point + 1
    for A in SAL:
        if A.y >= 900:
            print("hit")
            M.HIT()
            SAL.remove(A)
            print(M.health)
            if M.health == 0:
                pygame.display.update()
                messagebox.showwarning("FAIL","GAME OVER")
                pygame.quit()
                exit()
                    
                    
                    
                    
    if point == 5:
        pygame.display.update()
        messagebox.showwarning("Victory","now moving to level:3")
        pygame.quit()
        exit()



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                M.left = True
            if event.key == K_d:
                M.right = True
            if event.key == K_w:
                Q = Bullet(pygame.transform.scale(pygame.image.load("bullet.png"),(5,5)),M.x+22,M.y+22,5,5)
                BL.append(Q)
            
    

                
                

                    
                
                

                
        if event.type == KEYUP:
            if event.key == K_d:
                M.right = False
            if event.key == K_a:
                M.left = False
            if event.key == K_w:
                stay = True

            
                
                
                
                


    pygame.display.update()
