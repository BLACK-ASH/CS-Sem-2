from tkinter import *
root = Tk()

def colorChange(a):
    if(a==1):
        root.configure(background = "red")
    if(a==2):
        root.configure(background = "blue")
    if(a==3):
        root.configure(background = "green")

redButton = Button(text="RED" , command = lambda: colorChange(1),pady=5,padx=20)
redButton.place(x=150,y=100)

blueButton = Button(text="BLUE" , command=lambda:colorChange(2),pady=5,padx=20)
blueButton.place(x=150,y=300)

greenButton = Button(text="GREEN" , command=lambda:colorChange(3),pady=5,padx=20)
greenButton.place(x=150,y=200)

root.configure(background = "grey")
root.geometry("400x400")
root.mainloop()
