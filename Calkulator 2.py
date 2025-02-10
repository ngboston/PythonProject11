from tkinter import *

root = Tk()
root.title("Калькулятор")

number = 0
previous_number = 0
action = '+'

def make_action(chosen_action):
    global number
    global previous_number
    global action


    action = chosen_action
    previous_number = number
    number = 0
    entry_text.set(str(number))

def button_press_add():
    make_action('+')

def button_press_substract():
    make_action('-')

def button_press_multiply():
    make_action('*')

def button_press_divide():
    make_action('/')

def button_press_clear():
    global number
    global previous_number

    number = 0
    previous_number = 0

    entry_text.set(number)

def button_press_result():
    global number
    global previous_number
    global action


    if action == '+':
        number = previous_number + number
    elif action == '-':
        number = previous_number - number
    elif action == '*':
        number = previous_number * number
    elif action == '/':
        number = previous_number / number

    entry_text.set(number)

def add_digit(digit):
    global number

    number = number * 10 + digit

    entry_text.set(number)

def button_press_1():
    add_digit(1)

def button_press_2():
    add_digit(2)

def button_press_3():
    add_digit(3)

def button_press_4():
    add_digit(4)

def button_press_5():
    add_digit(5)

def button_press_6():
    add_digit(6)

def button_press_7():
    add_digit(7)

def button_press_8():
    add_digit(8)

def button_press_9():
    add_digit(9)

def button_press_0():
    add_digit(0)

Button(root, text='1', height=5, width=10, command=button_press_1).grid(row=1, column=0)
Button(root, text='2', height=5, width=10, command=button_press_2).grid(row=1, column=1)
Button(root, text='3', height=5, width=10, command=button_press_3).grid(row=1, column=2)
Button(root, text='4', height=5, width=10, command=button_press_4).grid(row=2, column=0)
Button(root, text='5', height=5, width=10, command=button_press_5).grid(row=2, column=1)
Button(root, text='6', height=5, width=10, command=button_press_6).grid(row=2, column=2)
Button(root, text='7', height=5, width=10, command=button_press_7).grid(row=3, column=0)
Button(root, text='8', height=5, width=10, command=button_press_8).grid(row=3, column=1)
Button(root, text='9', height=5, width=10, command=button_press_9).grid(row=3, column=2)
Button(root, text='=', height=5, width=10, command=button_press_result).grid(row=4, column=0)
Button(root, text='0', height=5, width=10, command=button_press_0).grid(row=4, column=1)
Button(root, text='AC', height=5, width=10, command=button_press_clear).grid(row=4, column=2)

Button(root, text='+', height=5, width=10, command=button_press_add).grid(row=1, column=3)
Button(root, text='-', height=5, width=10, command=button_press_substract).grid(row=2, column=3)
Button(root, text='*', height=5, width=10, command=button_press_multiply).grid(row=3, column=3)
Button(root, text='/', height=5, width=10, command=button_press_divide).grid(row=4, column=3)

entry_text = StringVar()
Entry(root, width=40, textvariable=entry_text).grid(row=0, column=0, columnspan=4)

root.mainloop()