from tkinter import *

root = Tk(className = " Canvas")
root.geometry("750x500")

c = Canvas (root,bg = "grey",height = 600 , width = 750)

# Body
body = c.create_oval(10,150,200,350,fill = "#0f51ff" )

# Head
headOutside = c.create_oval(10,10,200,200,fill = "#0f51ff")
headInside = c.create_oval(30,50,180,200,fill = "white")
nose = c.create_oval(95,90,110,105,fill = "red")

# Eye One
eye11 = c.create_oval(60,45,95,95,fill = "black")
eye12 = c.create_oval(61,43,95,93,fill = "white")
eye13 = c.create_oval(70,67,85,90,fill = "black")
eye13 = c.create_oval(73,70,81,86,fill = "white")

# Eye Two
eye11 = c.create_oval(110,45,142,95,fill = "black")
eye12 = c.create_oval(111,43,142,93,fill = "white")
eye13 = c.create_oval(118,65,133,90,fill = "black")
eye13 = c.create_oval(120,68,130,86,fill = "white")

# mouth
mouth = c.create_oval(65,135,145,170,fill = "red")
mouthInside = c.create_oval(75,155,135,170,fill = "#c62d42")

# noseLine
noseLine = c.create_line(103,106,103,135,fill = "black")
n11 = c.create_line(60,100,95,110)
n12 = c.create_line(60,115,95,115)
n13 = c.create_line(60,130,95,120)
n21 = c.create_line (115,110,145,100)
n22 = c.create_line (115,115,145,115)
n23 = c.create_line (115,120,145,130)

c.pack()

root.mainloop()
