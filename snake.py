import pygame
import random
import time
from pygame.locals import *
import all_button

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
def snake():
    foodX = (random.randint(0,1000)//50)*50
    foodY = (random.randint(0,1000)//50)*50
    snakeX = (random.randint(0,1000)//50)*50
    snakeY = (random.randint(0,1000)//50)*50
    snake = []
    snake.append([snakeX,snakeY])
    Sup = False
    Sdown = False
    Sright = False
    Sleft = False
    eat = False
    score = 0
    clock = pygame.time.Clock()
    change = 50
    def WiN(msg,x,y):
        fontobj = pygame.font.SysFont("freesans",50)
        msgobj = fontobj.render(msg,False,(0,0,255))
        screen.blit(msgobj,(x,y))
    def grid():
        for i in range(0,1050,50):
            pygame.draw.line(screen,(0,255,0),(i,0),(i,1000))
            pygame.draw.line(screen,(0,255,0),(0,i),(1000,i))
            
            


    while True:
        clock.tick(10)
        pygame.display.update()
        screen.fill((0,0,0))

        for q in snake:
            pygame.draw.rect(screen,(255,255,255),q+[50,50])
            
        grid()
        pygame.draw.rect(screen,(255,0,0),(foodX,foodY,50,50))
            





        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP and Sdown == False:
                    Sup = True
                    Sdown = False
                    Sright = False
                    Sleft = False  
                if event.key == pygame.K_DOWN and Sup == False:
                    Sup = False
                    Sdown = True
                    Sright = False
                    Sleft = False

                if event.key == pygame.K_RIGHT and Sleft == False:
                    Sup = False
                    Sdown = False
                    Sright = True
                    Sleft = False

                if event.key == pygame.K_LEFT and Sright == False:
                    Sup = False
                    Sdown = False
                    Sright = False
                    Sleft = True
        
            if event.type == QUIT:
                pygame.quit()
                exit()
        if Sup == True:
            snakeY = snakeY - change

        if Sdown == True:
            snakeY = snakeY + change

        if Sright == True:
            
            snakeX = snakeX + change

        if Sleft == True:
            snakeX = snakeX - change

        if snakeX > 1050:
            WiN("You Lose",400,450)
            pygame.display.update()
            
            time.sleep(3)
            all_button.allBUTTONS()


        if snakeX < -50:
            WiN("You Lose",400,450)
            pygame.display.update()
            time.sleep(3)
            all_button.allBUTTONS()

        if snakeY > 1000:
            WiN("You Lose",400,450)
            pygame.display.update()        
            time.sleep(3)
            all_button.allBUTTONS()
        if snakeY < -50:
            WiN("You Lose",400,450)
            pygame.display.update()        
            time.sleep(3)
            all_button.allBUTTONS()
        if [snakeX,snakeY] in snake[1:]:
            WiN("You Lose",400,450)
            pygame.display.update()        
            time.sleep(3)
            all_button.allBUTTONS()       
        if snakeX == foodX and snakeY == foodY:
            eat = True
            score = score + 1
            foodX = (random.randint(0,1000)//50)*50
            foodY = (random.randint(0,1000)//50)*50
            snake.append([snakeX,snakeY])
            print(len(snake))
        snake.insert(0,[snakeX,snakeY])
        snake.pop()
        pygame.display.update()

