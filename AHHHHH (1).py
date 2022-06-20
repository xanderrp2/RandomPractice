from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("300x300")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
CA = PhotoImage(file = "download.png")
AM = PhotoImage(file = "unnamed-1.png")

def INFO1():
    messagebox.showwarning("America","FOOD")
    
def INFO2():
    messagebox.showwarning("Canada","FOOD")
    
def INFO11():
    messagebox.showwarning("America","Climate")
    
def INFO21():
    messagebox.showwarning("Canada","climate")
    
def INFO12():
    messagebox.showwarning("America","animals")
    
def INFO22():
    messagebox.showwarning("Canada","animals")
   

def thing():
    x.add(FOOD,text = "FOOD")
    x.add(CLIMAT,text = "CLIMAT")
    x.add(ANIMALS,text = "ANIMALS")
    x.pack()

    
x = ttk.Notebook(root,width = 20, height = 200)
x.pack()




FOOD = ttk.Frame(x)
label = Label(FOOD,image = CA)
label.place(x = 0, y = 0)
button = Button(FOOD,text = "info",command = INFO1)
button.place(x = 150, y = 27)
label1 = Label(FOOD,image = AM)
label1.place(x = 0,y=58)
button1 = Button(FOOD,text = "info",command = INFO2)
button1.place(x = 150, y = 127)


CLIMAT = ttk.Frame(x)
label1 = Label(CLIMAT,image = CA)
label1.place(x = 0, y = 0)
button1 = Button(CLIMAT,text = "info",command = INFO11)
button1.place(x = 150, y = 27)
label11 = Label(CLIMAT,image = AM)
label11.place(x = 0,y=58)
button11 = Button(CLIMAT,text = "info",command = INFO21)
button11.place(x = 150, y = 127)



ANIMALS = ttk.Frame(x)
label2 = Label(ANIMALS,image = CA)
label2.place(x = 0, y = 0)
button2 = Button(ANIMALS,text = "info",command = INFO12)
button2.place(x = 150, y = 27)
label12 = Label(ANIMALS,image = AM)
label12.place(x = 0,y=58)
button12 = Button(ANIMALS,text = "info",command = INFO22)
button12.place(x = 150, y = 127)















thing()








root.mainloop()
