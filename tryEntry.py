from tkinter import *
from  tkinter import  ttk

from PIL.ImageOps import expand

root = Tk()
root.title("IT-Step")
root.geometry("400x350")

message = StringVar()
clicks = IntVar(value=0)



def click_btn():
    value = clicks.get()
    clicks.set(value + 1)

label = ttk.Label(textvariable= message)
label.pack(anchor=NW, padx=8, pady=8)

entry = ttk.Entry(textvariable=message)
entry.pack(anchor=NW, padx=8, pady=8)

btn = ttk.Button(textvariable= message)
btn.pack(anchor=NW, padx=8, pady=8)

btn2 = ttk.Button(textvariable= clicks,command=click_btn)
btn2.pack(anchor=CENTER, expand=1)

def check(*args):
    print(name)
    if name.get("admin"):
        result.set("Забороннене ім'я")
    else:
        result.set("норм")

root.mainloop()