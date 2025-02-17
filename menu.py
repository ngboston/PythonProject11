from tkinter import *
from tkinter import filedialog

def save_file():
    file_name = filedialog.asksaveasfilename(initialdir='/', title='Select file', filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))

    if file_name:
        f = open(file_name, 'w')
        text_save = text.get(1.0, END)
        f.write(text_save+'\n')
        f.close()

def open_file():
    file_name = filedialog.askopenfilename(initialdir='/', title='Open file', filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))

    if file_name:
        f = open(file_name, 'r')
        text_open = f.read()
        if text_open != None:
            text.delete(1.0, END)
            text.insert(END, text_open)

root = Tk()

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label='Open file as...', command=open_file)
file_menu.add_command(label='Save file as...', command=save_file)
file_menu.add_command(label='Exit', command=exit)

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='Help')
help_menu.add_command(label='About')

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Help", menu=help_menu)

text = Text(root)
text.pack(expand=YES, fill=BOTH)

root.mainloop()