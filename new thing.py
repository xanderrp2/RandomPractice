from tkinter import *
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
a = 0
b = 0
def cal():
    box2.delete(0,END)
    print(box1.get())
    print(box2.get())
    a = int(box1.get())
    b = (9/5)*a + 32
    print(b)
    box2.insert(0,b)
def rem():
    box1.delete(0,END)
    box2.delete(0,END)
    
    
    

button1 = Button(root,text = "calculate",height = 5, width = 10,command = cal)
button1.grid(row = 0,column = 9)
button2 = Button(root,text = "clear",height = 5, width = 10,command = rem)
button2.grid(row = 0,column = 3)
button3 = Button(root,text = "quit",command = exit,height = 5, width = 10)
button3.grid(row = 0,column = 180)
label1 = Label(root,text = "Far")
label1.grid(row = 5,column = 9)
label2 =  Label(root,text = "cel")
label2.grid(row = 5,column = 15)
box1 = Entry(root)
box1.grid(row = 18,column = 3)
box2 = Entry(root,text = b)
box2.grid(row = 18,column = 9)
root.mainloop()
