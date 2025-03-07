from tkinter import*
import mysql.connector as db

mydb = db.connect(
    host="localhost",
    user="root",
    password="root",
    database = "user"
)

cursor = mydb.cursor()

# Sign Up Page
root = Tk(className = "Sign Up")
root.geometry("300x200")

# Sign Up Page Variables
name = StringVar()
age = IntVar()
gender = StringVar() 

# Sign Up Page Labels
nameLabel = Label(root,text = "Name : ").grid(row = 1,column = 0)
nameEntry = Entry(root,textvariable = name).grid(row = 1,column = 1)

ageLabel = Label(root,text = "Age : ").grid(row = 2,column = 0)
ageEntry = Entry(root,textvariable = age).grid(row = 2,column = 1)

genderLabel = Label(root,text = "Gender : ").grid(row = 3,column = 0)
genderEntry = Entry(root,textvariable = gender).grid(row = 3,column = 1)

# Submit Function
def submit():
    cursor.execute("insert into userData values(%s,%s,%s)",(name.get(),age.get(),gender.get()))
    mydb.commit()
    print("Submitted",name.get(),age.get(),gender.get())

# Sign Up Page Buttons
signUp = Button(root,text = "Sign Up",command = submit)
signUp.grid(row=5,column=1)


root.mainloop()