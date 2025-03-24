import random
from itertools import count
from tkinter import  *

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e"}

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
                   16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2",
                   128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2",
                   1024: "#f9f6f2", 2048: "#f9f6f2"}

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
    while(matrix[a][b] != 0):
        a = random.randint(0, len(matrix) - 1)
        b = random.randint(0, len(matrix) - 1)
    matrix[a][b] = 2

def init_matrix():
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
                grid_cell[i][j].configure(text=str(matrix[i][j]), bg=BACKGROUND_COLOR_DICT[matrix[i][j]], fg=CELL_COLOR_DICT[matrix[i][j]])

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
    return (new, done)

def merge(mat):
    done = False
    for i in range(len(mat)):
        for j in range(len(mat) - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return (mat, done)

def left():
    global matrix
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    return done

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat)-j-1])
    return new

def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

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

def key_down(key):
    global matrix
    if key == KEY_UP:
        if up():
            add_two()
            update_grid_cell()
    elif key == KEY_DOWN:
        if down():
            add_two()
            update_grid_cell()
    elif key == KEY_LEFT:
        if left():
            add_two()
            update_grid_cell()
    elif key == KEY_RIGHT:
        if right():
            add_two()
            update_grid_cell()

def main():
    init_matrix()
    init_grid()
    update_grid_cell()
    root.bind('<Key>', lambda event: key_down(repr(event.char)))
    root.mainloop()

root = Tk()
root.title('2048')
main()