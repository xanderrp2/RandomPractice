from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("CATS")
root.geometry("400x400")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)
a= IntVar()
b= IntVar()
c= IntVar()
def pick():
button1= Checkbutton(root,text = "thi",variable = a)
button1.pack(side = TOP)
button2= Checkbutton(root,text = "thin",variable = b)
button2.pack(side = TOP)
button3 = Checkbutton(root,text = "think",variable = c)
button3.pack(side = TOP)
button3 = button(root,text = "cat",command = pick)
##a = IntVar()
##ac = IntVar()
##def care():
##    value = int(a.get())
##    if value == 0:
##        ac.set(int(box1.get())*20)
##
##    elif value == 1:
##        ac.set(int(box1.get())*10)
##      
##    elif value == 2:
##        ac.set(int(box1.get())*40)
##        
##    
##        
##
##def clear():
##    box2.delete(0,END)
##    box1.delete(0,END)
##
##
##
##button1 = Radiobutton(root,text="meat",value = 0,variable = a)
##button1.grid(row = 1,column =0,sticky = W)
##button2 = Radiobutton(root,text="vegitable",value = 1,variable = a)
##button2.grid(row = 2,column = 0,sticky = W)
##button3 = Radiobutton(root,text="candy",value=2,variable = a)
##button3.grid(row = 3,column = 0,sticky = W)
##buttonS1 =Button(root,text = "calculate",command = care)
##buttonS1.grid(row = 4,column = 2)
##buttonS2 = Button(root,text = "clear",command = clear)
##buttonS2.grid(row = 5,column = 2)
##lable1 = Label(root,text="amount")
##lable1.grid(row = 4,column = 0)
##label2 = Label(root,text="price")
##label2.grid(row = 5,column = 0)
##box1 = Entry(root)
##box1.grid(row = 4,column = 1)
##box2 = Entry(root,text = str(ac))
##box2.grid(row = 5,column =1)












##button1
##button2 = Radiobutton(root,text="cat",value = 1)
##button2.pack(side=LEFT)

root.mainloop()
