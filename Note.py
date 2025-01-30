# Блокнот с помощью tkinter

# Иморт библиотек
import tkinter
from tkinter.messagebox import showwarning
from tkinter import filedialog


# Функция изменения темы на светлую
def change_light_theme():
    text_field["bg"] = "white"
    text_field["fg"] = "black"
    text_field["insertbackground"] = "gray"
    text_field["selectbackgorund"] = "dodgerblue"


def create_new_file():
    file = open("")


# Функция изменения темы на тёмную
def change_dark_theme():
    text_field["bg"] = "black"
    text_field["fg"] = "violet"
    text_field["insertbackground"] = "brown"
    text_field["selectbackground"] = "#8D917A"


# Функция изменения шрифта на Arial
def change_arial_font():
    text_field["font"] = ("Arial", 14, "bold")


# Функция изменения шрифта на Bahnschrift
def change_bahnschrift_font():
    text_field["font"] = ("Bahnschrift", 14, "bold")


# Функция изменения шрифта на Times New Roman
def change_TNR_font():
    text_field["font"] = ("Times New Roman", 14, "bold")


# Функция выхода из приложения
def out():
    showwarning(title="Предупреждение",
                message="Независимо от того, куда вы нажмете, программа закроется(")
    window.destroy()


# Функция открытия файла
def open_file():
    file_path = filedialog.askopenfilename(title="Выбор файла",
                                           filetypes=(("Текстовые документы (*.txt)",
                                                       "*.txt"),
                                                      ("Все файлы",
                                                       "*.*")))
    text_field.delete("1.0", "end")
    text_field.insert("1.0", open(file_path,
                                  encoding="utf-8").read())


# Функция сохранения файла
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("Текстовые документы (*.txt)",
                                                         "*.txt"),
                                                        ("Все файлы",
                                                         "*.*")))
    file = open(file_path, "w", encoding="utf-8")
    text = text_field.get("1.0", "end")
    file.write(text)
    file.close()


# Создание и настройка окна
window = tkinter.Tk()
# photo = tkinter.PhotoImage(file="notepad.jpg")
# window.iconphoto(False, photo)
window.title("Notepad")
window.geometry("1280x720")

# Создание поля для печати
field = tkinter.Frame()
field.pack(fill="both", expand="1")

# Создание и настройка текста для поля печати
text_field = tkinter.Text(field,
                          bg="white",
                          fg="black",
                          padx=5,
                          pady=5,
                          wrap="word",
                          insertbackground="black",
                          selectbackground="dodgerblue",
                          font="Bahnschrift 14 bold")
# Размещение текста
text_field.pack(fill="both",
                side="left",
                expand="1")

# Создание колеса прокрутки
scroll = tkinter.Scrollbar(field,
                           command=text_field.yview)
scroll.pack(side="left",
            fill="y")
text_field.config(yscrollcommand=scroll.set)

# Создание области для размещение вкладок меню
main_menu = tkinter.Menu()

# Создание меню "Файл"
file_menu = tkinter.Menu(main_menu,
                         tearoff=0)

# Добавление подменю в меню "Файл"
file_menu.add_command(label="Новый",
                      )

file_menu.add_command(label="Открыть...",
                      command=open_file)

file_menu.add_command(label="Сохранить...",
                      )

file_menu.add_command(label="Сохранить как...",
                      command=save_file)

file_menu.add_command(label="Закрыть",
                      command=out)

# Создание меню "Вид"
view_menu = tkinter.Menu(main_menu,
                         tearoff=0)

# Создание подменю "Тема" в меню "Вид"
view_menu_sub = tkinter.Menu(view_menu,
                             tearoff=0)

# Создание подменю "Шрифт" в меню "Вид"
font_menu_sub = tkinter.Menu(view_menu,
                             tearoff=0)

# Добавление вариантов в подменю "Тема"
view_menu_sub.add_command(label="Тёмная",
                          command=change_dark_theme)

view_menu_sub.add_command(label="Светлая",
                          command=change_light_theme)
view_menu.add_cascade(label="Тема...",
                      menu=view_menu_sub)

# Добавление вариантов в подменю "Шрифт"
font_menu_sub.add_command(label="Arial",
                          command=change_arial_font)

font_menu_sub.add_command(label="Bahnschrift",
                          command=change_bahnschrift_font)

font_menu_sub.add_command(label="Times New Roman",
                          command=change_TNR_font)

view_menu.add_cascade(label="Шрифт...",
                      menu=font_menu_sub)

# Добавление меню "Файл" в область
main_menu.add_cascade(label="Файл",
                      menu=file_menu)
# добавление меню "Вид" в область
main_menu.add_cascade(label="Вид",
                      menu=view_menu)
# Размещение меню в окне
window.config(menu=main_menu)

window.mainloop()