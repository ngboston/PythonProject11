import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = tk.Entry(master, width=30, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            "C", "CE", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "="
        ]
        r = 1
        c = 0
        for button in buttons:
            command = lambda x=button: self.click(x)
            tk.Button(master, text=button, width=5, height=2, command=command).grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def click(self, key):
        if key == "C":
            self.entry.delete(0, "end")
        elif key == "CE":
            self.entry.delete(0, "end")
        elif key == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, "end")
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, "end")
                self.entry.insert(0, "Error")
        else:
            self.entry.insert("end", key)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()