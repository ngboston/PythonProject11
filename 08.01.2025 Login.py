from tkinter import *

root = Tk()
root.title("Вхід в рахунок")
root.geometry('400x300')

frame = Frame(
    root,
    padx=10,
    pady=10
)
frame.pack(expand=True)

log_1 = Label(
    frame,
    text="Введіть Логін "
)
log_1.grid(row=3, column=1)

pass_1 = Label(
    frame,
    text="Введить Пароль ",
)
pass_1.grid(row=4, column=1)

log_2 = Entry(
    frame,
)
log_2.grid(row=3, column=2, pady=5)

pass_2 = Entry(
    frame,
)
pass_2.grid(row=4, column=2, pady=5)

go_to = Button(
    frame,
    text="Вхів",
)
go_to.grid(row=5, column=2)

root.mainloop()