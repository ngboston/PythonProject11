import random
from itertools import count
from tkinter import *

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#bbada0"  # Changed background color
BACKGROUND_COLOR_CELL_EMPTY = "#cdc1b4"  # Changed empty cell color

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e", 4096: "#606000", 8192: "#600060"}  # Added more colors

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
                   16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
                   128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2",
                   1024: "#f9f6f2", 2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}  # Added more colors

FONT = ("Verdana", 40, "bold")

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"

mainframe = Frame()
grid_cell = []
matrix = []

def init_grid():
    backgraound = Frame(bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
    backgraound.grid()

    for i in range(GRID_LEN):
        grid_row = []
        for j in range(GRID_LEN):
            cell = Frame(backgraound, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
            cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
            t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=5, height=2)
            t.grid()
            grid_row.append(t)
        grid_cell.append(grid_row)

def add_two():
    a = random.randint(0, len(matrix) - 1)
    b = random.randint(0, len(matrix) - 1)
    while matrix[a][b] != 0:
        a = random.randint(0, len(matrix) - 1)
        b = random.randint(0, len(matrix) - 1)
    matrix[a][b] = 2

def init_matrix():
    global matrix
    matrix = []
    for i in range(GRID_LEN):
        matrix.append([0] * GRID_LEN)
    add_two()
    add_two()

def update_grid_cell():
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            if matrix[i][j] == 0:
                grid_cell[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
            else:
                grid_cell[i][j].configure(text=str(matrix[i][j]), bg=BACKGROUND_COLOR_DICT.get(matrix[i][j], "#000000"), fg=CELL_COLOR_DICT.get(matrix[i][j], "#FFFFFF"))

def cover_up(mat):
    new = []
    for i in range(len(mat)):
        new.append([0] * len(mat))
    done = False
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat)):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done

def merge(mat):
    done = False
    for i in range(len(mat)):
        for j in range(len(mat) - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return mat, done

def left():
    global matrix
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix, _ = cover_up(matrix)
    return done

def right():
    global matrix
    matrix = reverse(matrix)
    done = left()
    matrix = reverse(matrix)
    return done

def up():
    global matrix
    matrix = transpose(matrix)
    done = left()
    matrix = transpose(matrix)
    return done

def down():
    global matrix
    matrix = transpose(matrix)
    done = right()
    matrix = transpose(matrix)
    return done

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append(list(reversed(mat[i])))
    return new

def transpose(mat):
    new = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return new

def key_down(event):
    global matrix
    if event.keysym == 'Up':
        if up():
            add_two()
            update_grid_cell()
    elif event.keysym == 'Down':
        if down():
            add_two()
            update_grid_cell()
    elif event.keysym == 'Left':
        if left():
            add_two()
            update_grid_cell()
    elif event.keysym == 'Right':
        if right():
            add_two()
            update_grid_cell()

def new_game():
    global matrix
    init_matrix()
    update_grid_cell()

def main():
    root = Tk()
    root.title("2048 Game")
    root.resizable(False, False)

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New Game", command=new_game)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

    init_grid()
    init_matrix()
    update_grid_cell()

    root.bind('<Key>', key_down)
    root.mainloop()

if __name__ == "__main__":
    main()