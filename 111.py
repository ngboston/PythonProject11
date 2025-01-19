import tkinter as tk

# Створення головного вікна

root = tk.Tk()

root.title("Приклад Tkinter")

# Додавання мітки

label = tk.Label(root, text="Привіт, Tkinter!")

label.pack()

# Додавання кнопки

button = tk.Button(root, text="Натисни мене")

button.pack()

# Запуск головного циклу обробки подій

root.mainloop()