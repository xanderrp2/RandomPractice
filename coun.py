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
a1 = PhotoImage(file = "canada.png")
a2 = PhotoImage(file = "america.png")
def canadainfo(info):
    aq = StringVar()
    aq.set(info)
    
    frame1 = Frame(root,width = "300",height = "300",bg = "blue")
    frame1.place(x = 0,y = 0)
    label1 = Label(frame1,textvariable = aq)
    def forget():
            frame1.destroy()
            thing()
    label1.place(x = 50,y = 50)
    button1 = Button(frame1,text = "Back",command = forget)
    button1.place(x = 250,y = 150)
        
    

def thing():
        
    x = ttk.Notebook(root,width = 300, height = 300)

    x.place(x = 0,y = 0)
    a = ttk.Frame(x)
    label1 = Label(a,image = a1)
    label1.place(x = 0,y = 0)
    label2 = Label(a,image = a2)
    label2.place(x = 0,y = 109)
    button1 = Button(a,text = "canada?",command = lambda: canadainfo("canada food"))
    button1.grid(row = 3,column = 3,padx = 125,pady = 50)
    button2 = Button(a,text = "america?",command = lambda: canadainfo("american food"))
    button2.grid(row = 4,column = 3,padx = 125,pady = 50)
    b = ttk.Frame(x)
    label1 = Label(b,image = a1)
    label1.place(x = 0,y = 0)
    label2 = Label(b,image = a2)
    label2.place(x = 0,y = 109)
    button1 = Button(b,text = "canada?",command = lambda: canadainfo("canada animal"))
    button1.grid(row = 3,column = 3,padx = 125,pady = 50)
    button2 = Button(b,text = "america?",command = lambda: canadainfo("american animal"))
    button2.grid(row = 4,column = 3,padx = 125,pady = 50)

    c = ttk.Frame(x)
    label1 = Label(c,image = a1)
    label1.place(x = 0,y = 0)
    label2 = Label(c,image = a2)
    label2.place(x = 0,y = 109)
    button1 = Button(c,text = "canada?",command = lambda: canadainfo("canada size"))
    button1.grid(row = 3,column = 3,padx = 125,pady = 50)
    button2 = Button(c,text = "america?",command = lambda: canadainfo("american size"))
    button2.grid(row = 4,column = 3,padx = 125,pady = 50)
    x.add(a,text = "food")
    x.add(b,text = "animals")
    x.add(c,text = "size")
    root.mainloop()
thing()
