from tkinter import *
from tkinter import ttk

root = Tk()
root.title("It_step")
root.geometry("350x250")

for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(2): root.rowconfigure(index=r, weight=1)

btn1 = ttk.Button(text="button 1")
btn1.grid(row=0, column=0, columnspan=2, ipadx=70, padx=6, paaaady=6)

btn2 = ttk.Button(text="button 2")
btn2.grid(row=1, column=0,  ipadx=5, padx=6, paaaady=6)

btn3 = ttk.Button(text="button 3")
btn3.grid(row=1, column=1,ipadx=5, padx=6, paaaady=6)

root.mainloop()