from tkinter import *


def NewFile():
    name = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    text2save = "Це новий файл!"
    name.write(text2save)
    name.close


def OpenFile():
    name = filedialog.askopenfilename()
    print(name)


def About():
    print("Робота 10-А класу")


root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Новий", command=NewFile)
filemenu.add_command(label="Відкрити...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Вийти", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Допомога", menu=helpmenu)
helpmenu.add_command(label="Про програму", command=About)

mainloop()