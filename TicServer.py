import socket
import atexit
import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("game1")
SV = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def EXIT():
    print("this runs after keyboard interupt")
    SV.close()
atexit.register(EXIT)
HOST = ""
PORT = 12345
SV.bind((HOST,PORT))
SV.listen(5)
print("listen")
CONN,ADDR = SV.accept()
print(str(CONN) + str(ADDR))

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

    
##    HU = input("Server: ")
##    CONN.sendall(HU.encode())
##    HS = CONN.recv(1024)
##    print("Client: " + str(HS.decode()))
##    if HU == "Q":
##        print("quiting now")
##        SV.close()
    GaMe()
    pygame.display.update()

    




        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
        
