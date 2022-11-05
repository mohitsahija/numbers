from ast import Import
import tkinter as tk

from logging import root
from tkinter import *
root=Tk()
root.geometry("300x200")

W=Label(root,text="Gujarat University",font="50").pack()

Checkbutton1=tk.IntVar()
Checkbutton2=tk.IntVar()
Checkbutton3=tk.IntVar()

Button1=Checkbutton(root,text="Tutorial",variable=Checkbutton1,
onvalue=1,offvalue=0,height=2,width=10)
Button2=Checkbutton(root,text="Student",variable=Checkbutton2,
onvalue=1,offvalue=0,height=2,width=10)
Button3=Checkbutton(root,text="Courses",variable=Checkbutton3,
onvalue=0,offvalue=0,height=2,width=10)

Button1.pack()
Button2.pack()
Button3.pack()
root.mainloop()
