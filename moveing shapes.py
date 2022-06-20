import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
x = 0
s = 50
g = 100
h = 150
j = 200
k = 250
a = 300
x1 = 350
s1 = 400
g1 = 450
h1 = 500
j1 = 550
k1 = 600
a1 = 650
while True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),(x,0,50,50))
    if x == 1000:
        x = 0
    x = x + 50
    pygame.draw.rect(screen,(0,255,0),(s,50,50,50))
    if s == 1000:
        s = 0
    s = s + 50
    pygame.draw.rect(screen,(0,255,0),(g,100,50,50))
    if g == 1000:
        g = 0
    g = g + 50
    pygame.draw.rect(screen,(0,255,0),(h,150,50,50))
    if h == 1000:
        h = 0
    h = h + 50
    pygame.draw.rect(screen,(0,255,0),(j,200,50,50))
    if j == 1000:
        j = 0
    j = j + 50
    pygame.draw.rect(screen,(0,255,0),(k,250,50,50))
    if k == 1000:
        k = 0
    k = k + 50
    pygame.draw.rect(screen,(0,255,0),(a,300,50,50))
    if a == 1000:
        a = 0
    a = a + 50
    pygame.draw.rect(screen,(0,255,0),(x1,350,50,50))
    if x1 == 1000:
        x1 = 0
    x1 = x1 + 50
    pygame.draw.rect(screen,(0,255,0),(s1,400,50,50))
    if s1 == 1000:
        s1 = 0
    s1 = s1 + 50
    pygame.draw.rect(screen,(0,255,0),(g1,450,50,50))
    if g1 == 1000:
        g1 = 0
    g1 = g1 + 50
    pygame.draw.rect(screen,(0,255,0),(h1,500,50,50))
    if h1 == 1000:
        h1 = 0
    h1 = h1 + 50
    pygame.draw.rect(screen,(0,255,0),(j1,550,50,50))
    if j1 == 1000:
        j1 = 0
    j1 = j1 + 50
    pygame.draw.rect(screen,(0,255,0),(k1,600,50,50))
    if k1 == 1000:
        k1 = 0
    k1 = k1 + 50
    pygame.draw.rect(screen,(0,255,0),(a1,650,50,50))
    if a1 == 1000:
        a1 = 0
    a1 = a1 + 50
    pygame.draw.rect(screen,(0,255,0),(0,x,50,50))
    if x == 1000:
        x = 0
    x = x + 50
    pygame.draw.rect(screen,(0,255,0),(50,s,50,50))
    if s == 1000:
        s = 0
    s = s + 50
    pygame.draw.rect(screen,(0,255,0),(100,g,50,50))
    if g == 1000:
        g = 0
    g = g + 50
    pygame.draw.rect(screen,(0,255,0),(150,h,50,50))
    if h == 1000:
        h = 0
    h = h + 50
    pygame.draw.rect(screen,(0,255,0),(200,j,50,50))
    if j == 1000:
        j = 0
    j = j + 50
    pygame.draw.rect(screen,(0,255,0),(250,k,50,50))
    if k == 1000:
        k = 0
    k = k + 50
    pygame.draw.rect(screen,(0,255,0),(300,a,50,50))
    if a == 1000:
        a = 0
    a = a + 50
    pygame.draw.rect(screen,(0,255,0),(350,x1,50,50))
    if x1 == 1000:
        x1 = 0
    x1 = x1 + 50
    pygame.draw.rect(screen,(0,255,0),(400,s1,50,50))
    if s1 == 1000:
        s1 = 0
    s1 = s1 + 50
    pygame.draw.rect(screen,(0,255,0),(450,g1,50,50))
    if g1 == 1000:
        g1 = 0
    g1 = g1 + 50
    pygame.draw.rect(screen,(0,255,0),(500,h1,50,50))
    if h1 == 1000:
        h1 = 0
    h1 = h1 + 50
    pygame.draw.rect(screen,(0,255,0),(550,j1,50,50))
    if j1 == 1000:
        j1 = 0
    j1 = j1 + 50
    pygame.draw.rect(screen,(0,255,0),(600,k1,50,50))
    if k1 == 1000:
        k1 = 0
    k1 = k1 + 50
    pygame.draw.rect(screen,(0,255,0),(650,a1,50,50))
    if a1 == 1000:
        a1 = 0
    a1 = a1 + 50
    pygame.draw.circle(screen,(255,0,0),(500,500),5,1)
       
 
    
    







    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
