from tkinter import *
from  tkinter import  ttk

root = Tk()
root.title("IT-Step")
root.geometry("400x350")

def show_message():
    label["text"] = entry.get()

def clear():
    entry.delete(0, END)

ttk.Entry().pack(anchor=NW, padx=8, pady=8)

btn = ttk.Button(text="Click" , command=None )
btn.pack(anchor=NW, padx=8, pady=8)

label = ttk.Label(text="test")
label.pack(anchor=NW, padx=8, pady=8)

root.mainloop()
