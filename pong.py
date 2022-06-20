import pygame
import random
from pygame.locals import *
import all_button

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def pong():
    def WiN(msg,x,y):
        fontobj = pygame.font.SysFont("freesans",50)
        msgobj = fontobj.render(msg,False,(255,255,0))
        screen.blit(msgobj,(x,y))
    y = 300
    y2 = 300
    bx = 500
    by = 500
    px = 50
    px1 = 950
    player_L = 0
    player_R = 0
    lpu = False
    lpd = False
    rpu = False
    rpd = False
    u = 30


    change_x = 10
    ##start_x = -10
    ##Start_y = -10 
    ##false_y = 10
    ##true_y = 10
    change_y = random.randint(-10,+10)
    ##L_Y = [Start_y,change_y]
    ##L_X = [start_x,change_x]
    ##pick_x = random.choice(L_X)
    ##pick_y = random.choice(L_Y)




    while True:
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,255,255),(px,y,10,200))
        pygame.draw.rect(screen,(255,255,255),(px1,y2,10,200))
        pygame.draw.circle(screen,(0,0,255),(bx,by),u)
        WiN("player_L: " + str(player_L),250,50 )
        WiN("player_R: " + str(player_R),450,50 )
        bx = bx + change_x
        by = by + change_y






        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                xx = event.pos[0]
                yy = event.pos[1]
                print(xx,yy)
                if 0 < xx < 100 and 0 < yy < 100:
                    print("meow")
                    all_button.allBUTTONS()
                    
                    
            if event.type == KEYDOWN:
                if event.key == K_w:
    ##                y = y - 10
                    lpu = True
                if event.key == K_s:
    ##                y = y + 10
                    lpd = True
                if event.key == K_UP:
                    rpu = True
                if event.key == K_DOWN:
                    rpd = True
            if event.type == KEYUP:
                if event.key == K_w:

                    lpu = False
                if event.key == K_s:
                    lpd = False
                if event.key == K_UP:
                    rpu = False
                if event.key == K_DOWN:
                    rpd = False            
            if event.type == QUIT:
                pygame.quit()
                exit()
        if lpu == True:
            y = y - 10
        if lpd == True:
            y = y + 10
        if rpu == True:
            y2 = y2 - 10
        if rpd == True:
            y2 = y2 + 10
        if y <= 0:
            y = 0
        if y2 <= 0:
            y2 = 0
        if y >= 800:
            y = 800
        if y2 >= 800:
            y2 = 800
        if by-u <= 0 and by-u <= 0:
            change_y = - change_y
        if bx+u <= 0 and by-u <= 0:
            change_y = - change_y
        if bx+u >= 1000 and by+u >= 1000:
            change_y = - change_y
        if by+u >= 1000 and by+u >= 1000:
            change_y = - change_y
        if bx+u == 1000:
            bx = 500
            by = 500
            player_R = player_R + 1
        if bx-u == 0:
            bx = 500
            by = 500
            player_L = player_L + 1
        if bx+u == px1 and  y2+50 < by+u < y2+250:
            change_x = -change_x

        if px <= bx-u <+ px + 10 and y < by-u < y+250:
            print("please work")
            
            change_x = -change_x
        pygame.display.update()
        

    
