from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CALCULATOR")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
##message
##message
##message
ABC = 0
Q = str()
def Error0():
    print("cats")
    a = box1.get()
    b = box2.get()
    if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9":
        print("")
    elif type(a) == str or type(b) == str:
        messagebox.showerror("This is not a number","you can only enter numbers")
        
    
    
def PLUSS():
    global ABC
    Error0()
    print("hello")
    a = int(box1.get())
    b = int(box2.get())
    ABC = a + b
    print(str(ABC))
def MINUSS():
    global ABC
    Error0()
    a = int(box1.get())
    b = int(box2.get())
    ABC = a - b
    print(str(ABC))
def TIMESS():
    global ABC
    Error0()
    a = int(box1.get())
    b = int(box2.get())
    ABC = a*b
    print(str(ABC))
def DEVIDEE():
    global ABC
    Error0()
    a = int(box1.get())
    b = int(box2.get())
    if b == 0 or a == 0:
        messagebox.showerror("not divisable","you cannot devide a number by (0)")
    ABC = a/b
    print(str(ABC))
def EQUEL():
    global ABC
    Error0()
    print(str(ABC))
    box3.delete(0,END)
    Q = str(ABC)
    print(str(ABC))
    box3.insert(0,Q)
    print(Q)
    
def CLEAR():
    box1.delete(0,END)
    box2.delete(0,END)
    box3.delete(0,END)



frame1= Frame(root,width = "1000",height = "250",bg = "pink")
frame1.pack(side = TOP)
label = Label(root,text = "first number")
label.place(x=150,y = 100)
box1 = Entry(root)
box1.place(x=350,y=100)
frame2= Frame(root,width = "1000",height = "250",bg = "green")
frame2.pack(side = TOP)
label2 = Label(root,text = "second number")
label2.place(x=150,y = 350)
box2 = Entry(root)
box2.place(x=350,y=350)
frame3= Frame(root,width = "1000",height = "250",bg = "blue")
frame3.pack(side = TOP)
PLUS = Button(root, text = "+",width = "10",height = "10", command = PLUSS)
PLUS.place(x = 100, y = 575)
MINUS = Button(root, text = "-",width = "10",height = "10", command = MINUSS)
MINUS.place(x = 250, y = 575)
TIMES = Button(root, text = "x",width = "10",height = "10", command = TIMESS)
TIMES.place(x = 400, y = 575)
DEVIDE = Button(root, text = "/",width = "10",height = "10", command = DEVIDEE)
DEVIDE.place(x = 550, y = 575)
frame4= Frame(root,width = "1000",height = "250",bg = "red")
frame4.pack(side = TOP)
Equel = Button(root,text = "=",width = "20",height = "10",command = EQUEL)
Equel.place(x = 100,y=800)
box3 = Entry(root,textvariable = Q)
box3.place(x=300,y=800)
CLEAR = Button(root,text = "CLEAR",width = "20",height =  "10",command = CLEAR)
CLEAR.place(x=500,y=800)

root.mainloop()
