from tkinter import *
import webcolors

root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")

R = IntVar()
G = IntVar()
B = IntVar()



Slide_R = Scale(root,label = "RED", variable = R, from_=0, to= 255, orient = VERTICAL)
Slide_R.grid(row = 0,column = 0)
Slide_G = Scale(root,label = "RED", variable = G, from_=0, to= 255, orient = VERTICAL)
Slide_G.grid(row = 0,column = 1)
Slide_B = Scale(root,label = "RED", variable = B, from_=0, to= 255, orient = VERTICAL)
Slide_B.grid(row = 0,column = 2)


L = Label(root,bg = "black",width = 20,height = 20)
L.grid(row = 1, column = 0)
while True:
    Value = webcolors.rgb_to_hex((R.get(),G.get(),B.get()))
    L.config(bg = Value)
    root.update()
    


root.mainloop()
