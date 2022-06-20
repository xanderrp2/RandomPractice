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
class Charac():
    def __init__(self,image,x,y,width,height):
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height

    def showimage(self):
        screen.blit(self.image,(self.x,self.y))
        


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
class ship(Charac):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.right = False
        self.left = False
    def Move(self):
        if self.right == True and self.x <= 950 :
            self.x = self.x + 20
        if self.left == True and self.x >= 0:
            self.x = self.x - 20

class Bullet(Charac):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.Fal = False
        self.fire = False
    def shot(self):
        if self.fire == True:
            self.y = self.y - 20
l = 1
def LEVELONE():
    WINNOW = False


        
                
                


      
    M = ship(pygame.transform.scale(pygame.image.load("ship.png"),(50,50)),475,900,50,50)


    Fire = False          
    a = 10
    AL = []
    BL = []
    ##Q = Bullet(pygame.transform.scale(pygame.image.load("bullet.png"),(50,50)),M.x,M.y,50,50)  
    ##BL.append(Q)

    for i in range(0,9,1):

        A = alien(pygame.transform.scale(pygame.image.load("alien.png"),(50,50)),a,10,50,50)
        AL.append(A)
        B = alien(pygame.transform.scale(pygame.image.load("alien1.png"),(50,50)),a,110,50,50)
        AL.append(B)
        C = alien(pygame.transform.scale(pygame.image.load("alien3.png"),(50,50)),a,210,50,50)
        AL.append(C)
        a = a + 110
        if a >= 1000:
            a = 0
    ad = False
    al = False
    stay = False

    while True:
        screen.fill((0,0,0))
        for i in AL:
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
            for I in BL:
                for A in AL:
                    if A.x <= I.x <= A.x+100 and A.y <= I.y <= A.y + 100:
                        AL.remove(A)
                        BL.remove(I)
                        
        if len(AL) == 0 or WINNOW == True:
            pygame.display.update()
            messagebox.showwarning("Victory","now moving to level:2")
            l = 2
            break
            



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
                if event.key == K_r:
                    WINNOW = True

                    
                    

                        
                    
                    

                    
            if event.type == KEYUP:
                if event.key == K_d:
                    M.right = False
                if event.key == K_a:
                    M.left = False
                if event.key == K_w:
                    stay = True

                
                    
                    
                    
                    


        pygame.display.update()

