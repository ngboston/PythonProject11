import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Простий блокнот")

text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=tk.YES, fill=tk.BOTH)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Текстові файли", "*.txt"), ("Всі файли", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=root.quit)

root.mainloop()