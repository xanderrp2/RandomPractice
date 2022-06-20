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
        

class ship(Charac):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.right = False
        self.left = False
        self.health = 4
    def Move(self):
        if self.right == True and self.x <= 950 :
            self.x = self.x + 20
        if self.left == True and self.x >= 0:
            self.x = self.x - 20
    def HIT(self):
        self.health = self.health -1
        

class Bullet(Charac):
    def __init__(self,image,x,y,width,height,change):
        super().__init__(image,x,y,width,height)
        self.Fal = False
        self.fire = False
        self.change = change
    def shot(self):
        if self.fire == True:
            self.y = self.y + self.change
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
 
    def MOVE(self):
        self.x = self.x + self.change
        if self.x >= 1000 - self.width or self.x <= 0:
            self.y = self.y + 200
            self.change = -self.change
        
    def HIT(self):
        self.health = self.health - 1

class shooter(SupAlien):
    def __init__(self,image,x,y,width,height):
        super().__init__(image,x,y,width,height)
        self.change = 15
        self.health = 3
        self.shoot = random.randint(20,100)
        self.keep = 0
    def MOVE(self):
        self.x = self.x + self.change
        if self.x >= 1000 - self.width or self.x <= 0:
            self.y = self.y + 200
            self.change = -self.change
        self.keep = self.keep + 1
def LEVELTHREE():
    WINNOW = False

    SAL = []
    STAL = []


    A = SupAlien(pygame.transform.scale(pygame.image.load("alien.png"),(50,50)),100,100,50,50)
    SAL.append(A)




    H = shooter(pygame.transform.scale(pygame.image.load("alien1.png"),(50,50)),100,100,50,50)
    STAL.append(H)

                
                

    times = time.time()
      
    M = ship(pygame.transform.scale(pygame.image.load("ship.png"),(50,50)),475,900,50,50)


    Fire = False          
    a = 10
    BL = []
    ABL =[]
    ALD = 10
    AL = []
    M = ship(pygame.transform.scale(pygame.image.load("ship.png"),(50,50)),475,900,50,50)
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
            H = shooter(pygame.transform.scale(pygame.image.load("alien1.png"),(50,50)),100,100,50,50)
            STAL.append(H)
            times = time.time()



        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,255,255),(5,5,110,12))
        pygame.draw.rect(screen,(255,0,0),(7,7,(M.health*25),8))
        for i in SAL:
            i.showimage()
            i.MOVE()

        for i in STAL:
            i.showimage()
            i.MOVE()
            if i.keep == i.shoot:
                i.keep = 0
                J = Bullet(pygame.transform.scale(pygame.image.load("bullet.png"),(10,10)),i.x+22,i.y+22,5,5,20)
                ABL.append(J)
                print(len(ABL))
        M.showimage()
        M.Move()


        for I in ABL:
            I.showimage()
            I.fire = True
            I.shot()
            if I.y >= 1000:
                ABL.remove(I)

        for I in BL:
            I.showimage()
            I.fire = True
            I.shot()
            if I.y <= 0:
                BL.remove(I)
        for i in AL:
            i.showimage()
            i.MOVE()
        



        

        for I in BL:
            for A in AL:
                if A.x <= I.x <= A.x+100 and A.y <= I.y <= A.y + 100:
                    AL.remove(A)
                    BL.remove(I)  
        for A in ABL:
            if A.x <= M.x <= A.x+100 and A.y <= M.y <= A.y + 100:
                M.HIT()
                ABL.remove(A)
                if M.health == 0:
                    pygame.display.update()
                    messagebox.showwarning("FAIL","GAME OVER")
                    pygame.quit()
                    exit()
        for A in STAL:
            for I in BL:
                if A.x <= I.x <= A.x+100 and A.y <= I.y <= A.y + 100:
                    A.HIT()
                    BL.remove(I)
                    if A.health == 0:
                        STAL.remove(A)
                        point = point + 1
                        pygame.display.update()
        for A in SAL:
            for I in BL:
                if A.x <= I.x <= A.x+100 and A.y <= I.y <= A.y + 100:
                    A.HIT()
                    BL.remove(I)
                    if A.health == 0:
                        SAL.remove(A)
                        point = point + 1
                        pygame.display.update()
        for A in SAL:
            if A.y >= 900:
                M.HIT()
                SAL.remove(A)
                print(M.health)
                if M.health == 0:
                    pygame.display.update()
                    messagebox.showwarning("FAIL","GAME OVER")
                    pygame.quit()
                    exit()
        for A in STAL:
            if A.y >= 900:
                M.HIT()
                STAL.remove(A)
                print(M.health)
                if M.health == 0:
                    pygame.display.update()
                    messagebox.showwarning("FAIL","GAME OVER")
                    pygame.quit()
                    exit()
                        
                        
                        
                        
        if point == 5 or WINNOW == True:
            pygame.display.update()
            messagebox.showwarning("Victory","YOU WIN")




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
                    Q = Bullet(pygame.transform.scale(pygame.image.load("bullet.png"),(10,10)),M.x+22,M.y+22,5,5,-20)
                    BL.append(Q)
                if event.key == K_r:
                    WINNOW = True
                
        

                    
                    

                        
                    
                    

                    
            if event.type == KEYUP:
                if event.key == K_d:
                    M.right = False
                if event.key == K_a:
                    M.left = False


                
                    
                    
                    
                    


        pygame.display.update()


