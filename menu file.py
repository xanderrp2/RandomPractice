import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption("game1")
def WiN(msg,x,y):
    fontobj = pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg,False,(255,255,0))
    screen.blit(msgobj,(x,y))
    
def GaMe():
    screen = pygame.display.set_mode((900,900))
    x = 0
    y = 0
    u = (255,0,0)
    c = (0,0,255)
    Turn = 1
    HU = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}


    for i in range(0,3,1):
        for g in range(0,3,1):
                pygame.draw.rect(screen,(0,255,0),(x,y,300,300),5)
                x = x + 300
                u,c = c,u
                
        x = 0
        y = y + 300
        
            
            
    while True:







        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("first")
                (x,y) = event.pos
                ck = 1
                
                if 300 > x > 0 and 300 > y > 0 and HU[1] == "":
                    if Turn%2 == 1:
                        pygame.draw.line(screen,(255,0,0),(0,0),(300,300),5)
                        pygame.draw.line(screen,(255,0,0),(0,300),(300,0),5)
                        HU[1] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(150,150),150,5)
                        HU[1] = "O"
                        print(Turn)
                    Turn = Turn + 1
                        
                if 600 > x > 300 and 300 > y > 0 and HU[2] == "":
                    if Turn%2 == 1:
                        pygame.draw.line(screen,(255,0,0),(600,300),(300,0),5)
                        pygame.draw.line(screen,(255,0,0),(300,300),(600,0),5)

                        HU[2] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(450,150),150,5)
                        HU[2] = "O"
                    Turn = Turn + 1
                if 900 > x > 600 and 300 > y > 0 and HU[3] == "":
                    if Turn %2 == 1:
                        pygame.draw.line(screen,(255,0,0),(900,300),(600,0),5)
                        pygame.draw.line(screen,(255,0,0),(600,300),(900,0),5)
                
                        HU[3] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(750,150),150,5)
                        HU[3] = "O"

                    Turn = Turn + 1
                        
                if 300 > x > 0 and 600 > y > 300 and HU[4] == "":
                    if Turn%2 == 1:
                        pygame.draw.line(screen,(255,0,0),(0,300),(300,600),5)
                        pygame.draw.line(screen,(255,0,0),(300,300),(0,600),5)
                    
                        HU[4] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(150,450),150,5)
                        HU[4] = "O"

                    Turn = Turn + 1
                        
                if 600 > x > 300 and 600 > y > 300 and HU[5] == "":
                    if Turn%2 == 1:
                        pygame.draw.line(screen,(255,0,0),(300,300),(600,600),5)
                        pygame.draw.line(screen,(255,0,0),(600,300),(300,600),5)
                    
                        HU[5] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(450,450),150,5)

                        HU[5] = "O"
                        print(Turn)
                    Turn = Turn + 1
                        
                if 900 > x > 600 and 600 > y > 300 and HU[6] == "":
                    if  Turn%2 == 1:
                        pygame.draw.line(screen,(255,0,0),(600,300),(900,600),5)
                        pygame.draw.line(screen,(255,0,0),(900,300),(600,600),5)
                    
                        HU[6] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(750,450),150,5)
                        HU[6] = "O"
                        print(Turn)
                    Turn = Turn + 1
                        
                if 300 > x > 0 and 900 > y > 600 and HU[7] == "":
                    if Turn%2 == 1:
                
                        pygame.draw.line(screen,(255,0,0),(0,600),(300,900),5)
                        pygame.draw.line(screen,(255,0,0),(300,600),(0,900),5)
                    
                        HU[7] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(150,750),150,5)

                        HU[7] = "O"
                        print(Turn)
                    Turn = Turn + 1
                        
                if 600 > x > 300 and 900 > y > 600 and HU[8] == "":
                    if Turn%2 == 1:
                        pygame.draw.line(screen,(255,0,0),(300,600),(600,900),5)
                        pygame.draw.line(screen,(255,0,0),(600,600),(300,900),5)
                    
                        HU[8] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(450,750),150,5)


                        HU[8] = "O"
                        print(Turn)
                    Turn = Turn + 1
                if 900 > x > 600 and 900 > y > 600 and HU[9] == "":
                    if Turn%2 ==1:
                        pygame.draw.line(screen,(255,0,0),(600,600),(900,900),5)
                        pygame.draw.line(screen,(255,0,0),(900,600),(600,900),5)
                    
                        HU[9] = "X"
                        print(Turn)
                    else:
                        pygame.draw.circle(screen,(0,0,255),(750,750),150,5)

                        HU[9] = "O"
                        print(Turn)
                    Turn = Turn + 1
                print(HU)

            if event.type == QUIT:
                pygame.quit()
                exit()
        if HU[1] == HU[2] == HU[3] == "X":
            print(HU[1]+" wins")
            WiN(HU[1]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
        if HU[4] == HU[5] == HU[6] == "X":
            print(HU[4]+" wins")
            WiN(HU[4]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
        if HU[7] == HU[8] == HU[9] == "X":
            print(HU[7]+" wins")
            WiN(HU[7]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
        if HU[1] == HU[4] == HU[7] == "O":
            print(HU[1]+" wins")
            WiN(HU[1]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
        if HU[2] == HU[8] == HU[5] == "O":
            print(HU[2]+" wins")
            WiN(HU[2]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
            pygame.display.update()
        if HU[3] == HU[6] == HU[9] == "O":
            print(HU[3]+" wins")
            WiN(HU[3]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
            pygame.display.update()
        if HU[1] == HU[5] == HU[9] == "X":
            print(HU[1]+" wins")
            WiN(HU[1]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
        if HU[3] == HU[5] == HU[7] == "X":
            print(HU[3]+" wins")
            WiN(HU[3]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
        if HU[1] == HU[5] == HU[9] == "O":
            print(HU[1]+" wins")
            WiN(HU[1]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break

        if HU[3] == HU[5] == HU[7] == "O":
            print(HU[3]+" wins")
            WiN(HU[3]+" WIN",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break
            
        if("") not in list(HU.values()):
            print("tie")
            WiN("TIE you both lose.",450,450)
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()
            break


        pygame.display.update()






    






