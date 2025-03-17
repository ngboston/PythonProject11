from tkinter import *

from tkinter.ttk import Combobox


root = Tk()

root.title("Конвертер валю")


def F():

   v1 = Box_From.get()

   v2 = Box_To.get()

   m = float(Ent_From.get())

   if v1 == "UAH":

       if v2 == "USD":

           n = m / dollar

       elif v2 == "Eur":

           n = m / euro

       else:

           n = m

   elif v1 == "USD":

       if v2 == "Eur":

           n = m * dollar

       elif v2 == "Eur":

           n = m * dollar / euro

       else:

           n = m

   else:

       if v2 == "UAH":

           n = m * euro

       elif v2 == "USD":

           n = m * euro / dollar

       else:

           n = m

   Ent_To.delete(0, END)

   Ent_To.insert(0, n)


Lab_You = Label(text='Ви хочете конвертувати...').grid(row=0, column=1)

Lab_From = Label(text='зз:').grid(row=1, column=0)

Lab_To = Label(text='в:').grid(row=2, column=0)


V = ['UAH', 'USD', 'Eur']


Box_From = Combobox()

Box_From['values'] = V

Box_From.grid(row=1, column=1)

Box_To = Combobox()

Box_To['values'] = V

Box_To.grid(row=2, column=1)


Ent_From = Entry()

Ent_From.grid(row=1, column=2)

Ent_To = Entry()

Ent_To.grid(row=2, column=2)


Btn = Button(text='Підтвердити', command=F)

Btn.grid(row=3, column=1)


dollar = 41.70

euro = 43.49


root.mainloop()