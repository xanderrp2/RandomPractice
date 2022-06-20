from tkinter import *
from tkinter import messagebox
import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()
root = Tk()
root.title("CATS")
root.geometry("1000x1000")
root.resizable(width=True,height=True)
root.configure(bg="snow")
root.grid_columnconfigure(0,minsize = 50)
root.grid_rowconfigure(1,minsize = 50)

def SCOUT():
    
    global select
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    for i in data:
        print(i)
        select.insert(END,i)
    
button1 = Button(root,text = "PRESS THE BUTTON", command = SCOUT)
button1.pack()

scroll = Scrollbar(root,orient=VERTICAL)
select = Listbox(root,yscrollcommand=scroll.set, height=6)
scroll.config (command=select.yview)
scroll.pack(side=LEFT)
select.pack(side=LEFT)
root.mainloop()
