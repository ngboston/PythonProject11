from tkinter import *

root = Tk()  # Створюємо вікно
root.title("My first the window")  # Назва вікна
root.minsize(500, 300)
root.maxsize(800, 600)
root.geometry("600x400")
#root.geometry("600x400+200+300") відступи
root.resizable(0,0) # Як можна змінювати параметри вікна
root["bg"] = "orange"  # або код RGB . Заливка заднього фону

root.mainloop() # Завершення роботи звікном