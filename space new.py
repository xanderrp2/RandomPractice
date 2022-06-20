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

        
##        
##class ship():
##    def __init__(self,x,y):
##        self.x = x
##        self.y = y
##        self.image = SHIP1
##        self.right = False
##        self.left = False
##        
##    def draw(self):
##        screen.blit(self.image,(self.x,self.y))
##    def MOVE(self):
##        if self.right == True:
##            self.x = self.x + 20
##        if self.left == True:
##            self.x = self.x - 20            
##        
##class bullet():
##    def __init__(self,x,y):
##        self.x = x
##        self.y = y
##        self.fire = False
##    def draw(self):
##            pygame.draw.circle(screen,(255,255,255),(self.x,self.y),20)
##    def MOVE(self):
##        if self.fire == True:
##            self.y = self.y - 20
##        if self.fire == False:
##            self.y = 820
##class shot():
##    def __init__(self,y):
##        self.x = random.randint(220,880)
##        self.y = y
##        self.points = 0
##        self.KILL = True
##    def draw(self):
##        if self.KILL == False:
##            self.y = 325
##            
##        if (self.points == 5 or self.points == 10) and self.KILL == True:
##            pygame.draw.circle(screen,(25,55,255),(self.x,self.y),20)
##
##            
##            
##        
##    def MOVE(self):
##        if self.y >= 1000:
##            self.KILL = False
##            print("halloe")
##           
##            
##        if self.KILL == True:
##          self.y = self.y + 20
##        
##        
##        
##           
##            
##         
##
##alien1 = pygame.image.load("alien.png")
##alien01 = pygame.transform.scale(alien1,(100,100))
##alien13 = pygame.image.load("alien3.png")
##alien013 = pygame.transform.scale(alien13,(100,100))
##alien12 = pygame.image.load("alien2.png")
##alien012 = pygame.transform.scale(alien12,(100,100))
####alien1S = pygame.image.load("ship.png")
####alien01S = pygame.transform.scale(alien1S,(100,100))
##SHIP = pygame.image.load("ship.png")
##SHIP1 = pygame.transform.scale(SHIP,(75,75))
##Heart = pygame.image.load("download.png")
##Heart1 = pygame.transform.scale(Heart,(50,50))
##PLACE=[]
##PLACE2=[]
##PLACE3=[]
##HEALTH = {(0,30):Heart1,(0,80):Heart1,(0,130):Heart1}
##MU = []
##BEIT = 0
##a = 0
##HE = 30
##
##G = ship(450,800)
##P = bullet(G.x+20,G.y+20)
##JK = []
##for i in range(0,6,1):
##    a = a + 125
##    alien_1 = alien(a,300,alien01)
##    JK.append(a)
##    PLACE.append(alien_1)
##    alien_1 = alien(a,150,alien013)
##    JK.append(a)
##    PLACE2.append(alien_1)
##    alien_1 = alien(a,0,alien012)
##    JK.append(a)
##    PLACE3.append(alien_1)
## 
##    
##print(MU)
##a = 0
##kick = shot(325)
##
##b = 0
##sheald = True
##HITE = 0
##turn = 100
##
##
while True:
    A.draw()
##    
##    
##   
##    screen.fill((0,0,0))
##    if sheald == True:
##        pygame.draw.rect(screen,(255,255,255),(G.x - 7,G.y - 20,turn,10))
##    for al in HEALTH:
##        screen.blit(HEALTH[al],al)
##
##    
##    
##    
##    MU.append(P.x)
##    if P.fire:
##        for i in PLACE:
##                if i.x <= P.x <= i.x+100 and 300 <= P.y <= 400:
##                    print(MU[-1])
##                    
##                    print(kick.points)
##                    
##                    print(i)
##                    PLACE.remove(i)
##                    P.fire = False
##                    kick.points = kick.points + 1
##    if P.fire:
##        for w in PLACE2:
##                if w.x <= P.x <= w.x+100 and 150 <= P.y <= 250:
##                    print(MU[-1])
##             
##                    
##                    print(w)
##                    PLACE2.remove(w)
##                    P.fire = False
##                    kick.points = kick.points + 1
##    if P.fire:
##        for k in PLACE3:
##                if k.x <= P.x <= k.x+100 and 0 <= P.y <= 100:
##                    print(MU[-1])
##             
##                    
##                    print(k)
##                    PLACE3.remove(k)
##                    P.fire = False
##                    kick.points = kick.points + 1
##    if G.x < kick.x < G.x + 100 and G.y < kick.y < kick.y + 100:
##        KILL = False
##        HITE = HITE + 1
##        turn = turn - 50
##        kick.y = 325
##        kick.x = random.randint(120,780)
##        if HITE > 2:
##            sheald = False
##            
##            del(HEALTH[(0,HE)])
##            HE = HE + 50
##            kick.y = 325
##            kick.x = random.randint(120,780)
##            KILL = False
##    if len(HEALTH) ==0:
##        WiN("you lose",450,450)
##        pygame.display.update()
##        time.sleep(2)
##        exit()
##        pygame.quit()
##        
##        
##           
##
##            
##                
##    if kick.points == 10:
##        WiN("you win",450,450)
##        pygame.display.update()
##        time.sleep(2)
##        exit()
##        pygame.quit()
##    
##    
##    if BEIT == 18:
##        print("")
##    WiN(str(kick.points),0,0)
##    if kick.points == 5 :
##        KILL = True
##
##        
##        
##        kick.draw()
##
##        kick.MOVE()
##
##        
##    for i in PLACE:
##        i.draw()
##        i.MOVE()
##        if i.x >=900:
##            i.change = -i.change
##        if i.x <=0:
##            i.change = -i.change
##        if i.times >= 3:
##            i.change = - i.change
##            i.times = 0
##    for i in PLACE2:
##        i.draw()
##        i.MOVE()
##        if i.x >=900:
##            i.change = -i.change
##        if i.x <=0:
##            i.change = -i.change
##        if i.times >= 3:
##            i.change = - i.change
##            i.times = 0
##    for i in PLACE3:
##        i.draw()
##        i.MOVE()
##        if i.x >=900:
##            i.change = -i.change
##        if i.x <=0:
##            i.change = -i.change
##        if i.times >= 3:
##            i.change = - i.change
##            i.times = 0
##    for i in PLACE:
##        if P.x <= i.x and P.x >= i.x + 200:
##            print("T")
##    P.x = G.x + 25
##    
##     
##        
##    P.draw()
##    P.MOVE()
##    G.draw()
##    G.MOVE()
##    if P.y <= 0:
##        P.fire = False
##     
##    
##    
##
##
##
##
##    ##print(MU[-1])
##
##
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
##        if event.type == KEYDOWN:
##            if event.key == K_SPACE:
##                P.fire = True
##                print("Y")
##            if event.key == K_RIGHT:
##                G.right = True
##            if event.key == K_LEFT:
##                G.left = True
##                
##        if event.type == KEYUP:
##            if P.fire == False:
##                if event.key == K_SPACE:
##                    P.fire = False
##                           
##            if event.key == K_RIGHT:
##                G.right = False
##                
##            if event.key == K_LEFT:
##                G.left = False
##
##    pygame.display.update()
##
##
##    
##
##while True:
##
##
##
##
##
##
##
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()

    pygame.display.update()
