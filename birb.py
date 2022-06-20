from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a = IntVar()
q = StringVar()
a.set(0)
def call():
    if a.get() == 1:
        q.set("this is a dog")
    elif a.get() == 2:
        q.set("this is a cat")
    elif a.get() == 3:
        q.set("this is a bird")
label = Label(root, text = "pick a topic")
label.grid(row = 1,column = 1,columnspan = 2,pady = 1,padx = 1)
button1 = Radiobutton(root,text = "dogs",value = 1,variable = a,command = call)
button1.grid(row = 2,column = 1,pady = 1,padx = 1)
button2 = Radiobutton(root,text = "cats",value = 2,variable = a,command = call)
button2.grid(row = 3,column = 1,pady = 1,padx = 1)
button3 = Radiobutton(root,text = "birds",value = 3,variable = a,command = call)
button3.grid(row = 4,column = 1,pady = 1,padx = 1)
label2 = Message(root,textvariable = q)
label2.grid(row = 5,column = 1,columnspan = 3,rowspan = 3,pady = 1,padx = 1)


root.mainloop()
