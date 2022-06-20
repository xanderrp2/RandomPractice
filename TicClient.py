import socket
import atexit
import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
HOST = "localhost"
PORT = 12345
CV = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def EXIT():
    print("this runs after keyboard interupt")
    CV.close()
atexit.register(EXIT)
CV.connect((HOST,PORT))
print("connected")

def GaMe():
    screen = pygame.display.set_mode((900,900))
    x = 0
    y = 0
    u = (255,0,0)
    c = (0,0,255)
    Turn = 0
    HU = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}


    for i in range(0,3,1):
        for g in range(0,3,1):
                pygame.draw.rect(screen,(0,255,0),(x,y,300,300),5)
                x = x + 300
                u,c = c,u
                
        x = 0
        y = y + 300

while True:

    
##    CS = CV.recv(1024)
##    print("Server: " + str(CS.decode()))
##    CU = input("client: ")
##    CV.sendall(CU.encode())
##    if CU == "Q":
##        CV.close()
    GaMe()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()



            

    pygame.display.update()
