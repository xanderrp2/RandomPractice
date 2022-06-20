import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
x = 0
##y = 0
##x2 = 950
clock = pygame.time.Clock()
##h = random.randint(0,255)
##g = random.randint(0,255)
##h = random.randint(0,255)
##red = (255,0,0)
##blue = (0,0,255)
##green = (0,255,0)
##colors = [red,green,blue]
##change = 10
##x3 = 50
##x4 = 150
##x2 = 0
y1 = 1000
y2 = 1000
y3 = 900
while True:
##  clock.tick(10)
    screen.fill((0,0,0))
##    pygame.draw.rect(screen,(random.choice(colors)),(x,y,50,50))
##    pygame.draw.rect(screen,(random.choice(colors)),(x2,y,50,50))
##    y = y + 50
##    x = x + 50
##    x2 = x2 - 50
##    if y == 1000:
##        y = 0
##        x = 0
##        x2 = 950
##    
##    pygame.draw.circle(screen,(0,255,0),(500,500),x)
##    x = x + change
##    if x == 500:
##        change = - 10
##        x = x + change
##    elif x == 0:
##        change = 10
##        x = x + change

    pygame.draw.circle(screen,(0,0,255),(200,y1),25,5)
    pygame.draw.circle(screen,(0,0,255),(100,y2),25,5)
    pygame.draw.rect(screen,(0,255,0),(50,y3,200,100))
    y1 = y1 - 10
    y2 = y2 - 10
    y3 = y3 - 10
    if y3 == 0:
        y1 = 1000
        y2 = 1000
        y3 = 900
        
    
##    x3 = x3 + 10
##    x4 = x4 + 10
##    x2 = x2 + 10
##    if x2 == 800:
##        x3 = 50
##        x4 = 150
##        x2 = 0
        

    






    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
