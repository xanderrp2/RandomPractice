from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("200x440")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
Cal = StringVar()
M = []
k = ""
DE = []
RUN = 1


class BUTTON():
    global M
    global Cal
    
    def __init__(self,text,colour,width,height,row,column,command):
        self.text = text
        self.colour = colour
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.command = command
        if self.command == "outprint":
            self.button = Button(root,text = text,bg = colour,width = width, height = height,command = self.outprint)
        else:
            self.button = Button(root,text = text,bg = colour,width = width, height = height,command = command)
        
        self.button.grid(row = row,column = column)
    def outprint(self):
        a = self.text
        M.append(str(a))
        global A
        A = "".join(M)
        print(A +"#3")
        Cal.set(A)
        print(str(M)+"#1")
        print(str(a)+"#2")
        
    def active(self):
        global A
        global DE
        DE.append(A)
        print(str(DE) + "#4")
        Cal.set("")
        for i in range(0,len(M),1):
            M.remove(M[0])
        
            
    def devision(self):
        self.active()
        global RUN
        RUN = 1

        
    def multi(self):
        self.active()
        global RUN
        RUN = 2
    def minus(self):
        self.active()
        global RUN
        RUN = 3

        
        
        
    def equle(self):
        self.active()
        global RUN
        global B
        global DE
        global A
        
        
        if RUN == 1:
            self.active()
            
            B = int(DE[0])
            for i in range(1,len(DE)-1,1):
                B = B/int(DE[i])
                
                print(B)
            Cal.set(str(B))
            
        elif RUN ==2:
            self.active()
            
            B = int(DE[0])
            for i in range(1,len(DE)-1,1):
                B = B*int(DE[i])
                
                print(B)
            Cal.set(str(B))
        elif RUN == 3:
            self.active()
            B = int(DE[0])-int(DE[1])
            print(B)
            print(RUN)
        Cal.set(str(B))
        for i in range(0,len(DE),1):
            DE.remove(DE[0])
        
        

        
for i in range(0,3,1):
    A1 = BUTTON(str(i),"orange",5,5,2,i,"outprint")
for i in range(0,3,1):
    A1 = BUTTON(str(i+3),"orange",5,5,3,i,"outprint")
for i in range(0,3,1):
    A1 = BUTTON(str(i+6),"orange",5,5,4,i,"outprint")
output = Label(root,textvariable = Cal,width = 10,height = 5)
output.grid(row = 1,column = 0,columnspan = 4)
A2 = BUTTON(".","orange",5,5,5,0,"outprint")
A2 = BUTTON("9","orange",5,5,5,1,"outprint")
A2 = BUTTON("/","orange",5,5,2,4,A2.devision)
A2 = BUTTON("x","orange",5,5,3,4,A2.multi)
A2 = BUTTON("-","orange",5,5,4,4,A2.minus)
A2 = BUTTON("=","orange",5,5,5,4,A2.equle)

        







root.mainloop()
