from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle

HEIGHT = 550
WIDTH = 550

def registration():
    label_error = None

    frame = Frame(root, bd=10)
    frame.place(relx=.5, rely=.2, relheight=.6, relwidth=.7, anchor='n')

    # sign in віджет
    label = Label(frame, text="Sign Up", font='16')
    label.place(relwidth=1, relheight=.1)

    # Login
    label_login = Label(frame, text="Login")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

    #Password
    label_password1 = Label(frame, text="Password: ")
    label_password1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show='*')
    password1.place(relx=0.4, rely=0.4, relwidth=0.55, relheight=0.1)

    #Confirm pass
    label_password2 = Label(frame, text="Confirm Pass: ")
    label_password2.place(rely=0.6, relwidth=0.35, relheight=0.1)

    password2 = Entry(frame, show='*')
    password2.place(relx=0.4, rely=0.6, relwidth=0.55, relheight=0.1)

    #Button
    button = Button(frame, text="Sign Up", command=lambda: signup())
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)

    def signup():
        nonlocal label_error
        error = ''

        if label_error:
            pass
           #label_error.destroy()

        if len(login_register.get()) == 0:
            error = '*login error'
        elif len(password1.get()) < 6:
            error = '*password error, need 6 char'
        elif not password1.get() == password2.get():
            error = '*password error'
        else:
            save()

        label_error = Label(frame, text=error, fg='red')
        label_error.place(rely=0.7)

    def save():
        data = dict()
        data[login_register.get()] = password1.get()
        f = open('login.txt', 'wb')
        pickle.dump(data, f)
        f.close()
        login_form()


def login_form():
    frame = Frame(root, bd=10)
    frame.place(relx=.5, rely=.2, relheight=.6, relwidth=.7, anchor='n')

    # Sign in віджет
    label = Label(frame, text="Sign In", font='16')
    label.place(relwidth=1, relheight=.1)

    # Login
    label_login = Label(frame, text="Login: ")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

    # Password
    label_password = Label(frame, text="Password: ")
    label_password.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password = Entry(frame, show='*')
    password.place(relx=0.4, rely=0.4, relwidth=0.55, relheight=0.1)

    # Button
    button = Button(frame, text="Sign In", command=lambda: login_pass())
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)

    def login_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if login_register.get() in a and password.get() == a[login_register.get()]:
            messagebox.showinfo("Login Successful", "You are now logged in!")
        else:
            messagebox.showinfo("Login Failed", "You are not logged in!")

root = Tk()
root.title('Login Form')
root.geometry("%dx%d" % (WIDTH, HEIGHT)) #root.geometry("550x550")
root.resizable(False, False)

root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

img = PhotoImage(file='img/bg2.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_singup = Button(root, text="SIGN UP", bg='gold', command=registration)
button_singup.place(relx=0.2, rely=0.1, relwidth=0.3)

button_signin = Button(root, text="SIGN IN", bg='gold', command=login_form)
button_signin.place(relx=0.5, rely=0.1, relwidth=0.3)



root.mainloop()