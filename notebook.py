from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
label2V = StringVar()
label2V2 = StringVar()
label2V2V = StringVar()
score = 0
rot = StringVar()
label14 = Label(root,textvariable = rot)
label14.pack()
def thing():
    x.add(a,text = "Question #1")
    x.add(b,text = "Question #2")
    x.add(c,text = "Question #3")
    x.pack()
def COR():
    global score
    label2V.set("correct")
    score = score+1
    rot.set("Score = "+str(score))
def COr():
    global score
    label2V2.set("correct")
    score = score+1
    rot.set("Score = "+str(score))
def Cor():
    global score
    label2V2V.set("correct")
    score = score+1
    rot.set("Score = "+str(score))
def INC():
    label2V.set("incorrect")
def INc():
    label2V2.set("incorrect")
def Inc():
    label2V2V.set("incorrect")

x = ttk.Notebook(root,width = 20, height = 100)

a = ttk.Frame(x)
label2 = Label(a,textvariable = label2V)
label2.grid(row = 1, column = 3, columnspan = 2,padx = 10)
label1 = Label(a, text = "which is better?",width = 10)
label1.grid(row = 2,column = 2, columnspan = 4,padx = 2)
button1 = Button(a,text = "dogs",width = 10, height = 2,command = COR)
button1.grid(row = 3, column = 1,columnspan = 3,padx = 40)
button2 = Button(a,text = "cats",width = 10, height = 2,command = INC)
button2.grid(row = 3,column = 4, columnspan = 3,padx = 2)

b = ttk.Frame(x)
label2 = Label(b,textvariable = label2V2)
label2.grid(row = 1, column = 3, columnspan = 2,padx = 10)
label1 = Label(b, text = "which is better?",width = 10)
label1.grid(row = 2,column = 2, columnspan = 4,padx = 2)
button1 = Button(b,text = "cars",width = 10, height = 2,command = INc)
button1.grid(row = 3, column = 1,columnspan = 3,padx = 40)
button2 = Button(b,text = "trees",width = 10, height = 2,command = COr)
button2.grid(row = 3,column = 4, columnspan = 3,padx = 2)

c = ttk.Frame(x)
label2 = Label(c,textvariable = label2V2V)
label2.grid(row = 1, column = 3, columnspan = 2,padx = 10)
label1 = Label(c, text = "which is better?",width = 10)
label1.grid(row = 2,column = 2, columnspan = 4,padx = 2)
button1 = Button(c,text = "animals",width = 10, height = 2,command = Cor)
button1.grid(row = 3, column = 1,columnspan = 3,padx = 40)
button2 = Button(c,text = "rocks",width = 10, height = 2,command = Inc)
button2.grid(row = 3,column = 4, columnspan = 3,padx = 2)






thing()
root.mainloop()
