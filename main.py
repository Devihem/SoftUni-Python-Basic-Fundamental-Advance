import tkinter as tk
import copy

def visualize_maze(maze_lst):
    cell_size = 20
    canvas_width = len(maze_lst[0]) * cell_size
    canvas_height = len(maze_lst) * cell_size

    root = tk.Tk()
    root.title("Maze Visualization")
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    for row in range(len(maze_lst)):
        for col in range(len(maze_lst[row])):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            symbol = maze_lst[row][col]

            if symbol == "#":
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            elif symbol == "k":
                canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

    root.mainloop()

def kate_position(maze_lst):
    kate_state = True
    for row in range(len(maze_lst)):
        for col in range(len(maze_lst[row])):
            if maze_lst[row][col] == "k":
                if row == 0 or row == len(maze_lst) - 1:
                    if col == 0 or col == len(maze_lst[row]) - 1:
                        kate_state = False
                    elif row == 0:
                        if maze_lst[row][col + 1] != " " and maze_lst[row + 1][col] != " ":
                            kate_state = False
                    elif row == len(maze_lst) - 1:
                        if maze_lst[row][col + 1] != " " and maze_lst[row - 1][col] != " ":
                            kate_state = False
                elif col == 0 or col == len(maze_lst[row]) - 1:
                    if row == 0 and len(maze_lst) > 1:
                        if maze_lst[row - 1][col] != " ":
                            kate_state = False
                    elif row == len(maze_lst) - 1:
                        if maze_lst[row + 1][col] != " ":
                            kate_state = False
                    else:
                        if maze_lst[row - 1][col] != " " and maze_lst[row + 1][col] != " ":
                            kate_state = False
                return row, col, kate_state
    else:
        row, col = "END", "END"
        return row, col, kate_state

def kate_move_direction(k_row, k_col, maze_lst, moves):
    path_symbol = " "
    replace_symbol = "-"
    step = 1

    while True:
        if k_row != 0 and maze_lst[k_row - 1][k_col] == path_symbol:
            maze_lst[k_row - 1][k_col] = "k"
            maze_lst[k_row][k_col] = replace_symbol
            break
        elif k_row != len(maze_lst) - 1 and maze_lst[k_row + 1][k_col] == path_symbol:
            maze_lst[k_row + 1][k_col] = "k"
            maze_lst[k_row][k_col] = replace_symbol
            break
        elif k_col
