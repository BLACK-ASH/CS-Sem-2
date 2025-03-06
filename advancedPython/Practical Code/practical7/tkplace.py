import tkinter as tk

root = tk.Tk()
root.title("place layout example")
root.geometry("300x300+50+100")

def display_selection(event):
    selection= cities_listbox.curselection()
    print(cities_listbox.get(selection))

tk.Label(
    root,
    text="which of the following cities would you like to travel to?",
    wraplength = 200,
    ).place(x=50, y=20)

cities_listbox =tk.Listbox(root,selectmode = tk.BROWSE,width=24)
cities_listbox.place(x=40, y=65)

cities =["new york","singapore","dubai","mumbai","tokyo"]
for city in cities:
    cities_listbox.insert(tk.END,city)

cities_listbox.bind("<<ListboxSelect>>",display_selection)

end_button = tk.Button(root, text="End",command=quit)
end_button.place(x=125,y=250)

root.mainloop()