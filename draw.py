from tkinter import *

root = Tk()
S=Scrollbar(root)
T = Text(root, height = 4, width = 50)
S.pack(side = RIGHT,fill = Y)
T.pack(side = LEFT, fill=Y)
S.config(yscrollcommand=S.set)
T.config(yscrollcommand=S.set)
quote = """Hamlet: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The siblings and arrows of outrageuous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more-- and by a sleep to say we emd
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished"""
T.insert(END, quote)
mainloop( )








##from tkinter import *
##
##widthC = 500
##heightC =150
##
##def paint(event):
##    python_green = "#476042"
##    x1, y1 = (event.x - 1),(event - y)
##    x2, y2 = (event.x + 1),(event + y)
##    w.create_oval(x1,y1,x2,y2,fill="python_green")
##master = Tk()
##master.title("Painting using ovals")
##w = Canvas(master, width=widthC,height=heightC)
##w.pack(expand = YES,fill = BOTH)
##w.bind("",paint)
##message = Label(master,text = "press and drag the mouse to draw")
##message.pack(side = BOTTOM)
##mainloop()





##from tkinter import *
##
##canvas_width = 190
##canvas_height = 150
##
##master = Tk()
##
##w = Canvas(master,width=canvas_width,height=canvas_height)
##w.pack
##w.create_oval(0,0,100,100,fill="blue")
##mainloop()





##from tkinter import *
##master  = Tk()
##w = Canvas(master, width=200, height=100)
##
##w.pack()
##
##w.create_rectangle(50,20,150,80, fill="#476042")
##w.create_rectangle(65, 35, 135, 65, fill="yellow")
##w.create_line(0,0,50,20,fill="blue", width= 3)
##w.create_line(0,100,50,80,fill="blue", width= 3)
##w.create_line(150,20,200,0,fill="blue", width= 3)
##w.create_line(150,80,200,100,fill="blue", width= 3)
##
##mainloop()





##from tkinter import *
##master = Tk()
##
##canvas_width = 800
##canvas_height = 400
##w = Canvas(master,width=canvas_width,height=canvas_height)
##w.pack()
##y = int(canvas_height / 2)
##w.create_line(0,y,canvas_width, y, fill="#476042")
##
##mainloop()
