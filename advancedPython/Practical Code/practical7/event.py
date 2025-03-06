from tkinter import*
from tkinter.ttk import*
import tkinter as tk

root = Tk()
root.geometry("200x100")

def pressed2(event):
     print('Button-2 pressed at x = %d, y= %d' %(event.x, event.y))

def pressed3(event):
    print('Button-3 pressed at x = %d, y= %d' %(event.x, event.y))

def double_click(event):
    print('Double clicked at x = %d, y= %d' %(event.x, event.y))

frame1 =Frame(root, height =100, width = 200)

frame1.bind('<Button-1>',pressed2)
frame1.bind('<Double 1>', double_click)

frame1.pack()

mainloop()
