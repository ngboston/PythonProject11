from tkinter import *

root = Tk()
root["bg"] = "orange"

# root.mainloop()  Створюються два послідовних вікна

root1 = Tk()
root1["bg"] = "blue"

root.mainloop()
root1.mainloop() # Створюються два паралельних вікна