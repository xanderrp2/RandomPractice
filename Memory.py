from tkinter import *
import webcolors
from tkinter import messagebox
import pygame
import random
import time
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
A = 0

FirstHalf = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
SecondHalf = []
for i in range(1,17,1):
    imageA = PhotoImage(file = "Pokemon"+str(i)+".png")
    SecondHalf.append((imageA,FirstHalf[i-1]))

imageB = PhotoImage(file = "Question.png")
random.shuffle(SecondHalf)
Clicked = []
Objects = []
Solved = []
Ccounter = 0
TimeNow = time.time()
Flag = True
class Tiles():
    def __init__(self,row,column,Image,state,number,ID):
        self.row = row
        self.column = column
        self.Image = Image
        self.state = 0
        self.number = number
        self.ID = ID
    def show_Tile(self):
        self.Tile = Button(root,image = imageB,command = self.States)
        self.Tile.grid(row = self.row,column = self.column)
    def States(self):
        global Ccounter
        Ccounter = Ccounter + 1
        if self.state == 0:
            self.state = 1
        self.Tile.configure(image = self.Image)
        root.update()
        time.sleep(0.5)
        Clicked.append(self.ID)
        if Ccounter%2 == 0:
            if len(Clicked) == 2 and Clicked[-1][-1] == Clicked[-2][-1]:
                for CL in Clicked:
                    for Ob in Objects: 
                        if CL == Ob.ID:# (Ob) this was an object however the attribute "ID" stores the tuples from the list positions.
                            Ob.state = 2
                            Solved.append(Ob)
                        
                                
                Clicked.pop(-1)
                Clicked.pop(-1)
                RUN()            
            else:
                Clicked.pop(-1)
                Clicked.pop(-1)
                RUN()
    def Clear(self):
        if self.state == 1:
            self.state == 0
            self.Tile.configure(image = imageB)
def RUN():
        if len(Clicked) == 0:
            for Ob in Objects:
                Ob.Clear()
for i in range(0,4,1):
    for g in range(0,4,1):
        TileA = Tiles(i,g,SecondHalf[A][0],0,A,SecondHalf[A])
        TileA.show_Tile()
        Objects.append(TileA)   
        A = A + 1

while Flag:
    root.update()
    TimeFinish = time.time()
    ENDHERE = TimeFinish-TimeNow
    if len(Solved) == 16:
        messagebox.showwarning("GOOD GAME","GAME WON!!!" + str(ENDHERE))
        Flag = False
        
    

root.mainloop()



        







