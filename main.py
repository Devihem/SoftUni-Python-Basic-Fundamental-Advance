import tkinter as tk
from tkinter import messagebox

# function to check for a winner
def winner_check(grid_list: list, l_column: int, l_row: int):
    if grid_list[l_row][0] == grid_list[l_row][1] == grid_list[l_row][2] or \
            grid_list[0][l_column] == grid_list[1][l_column] == grid_list[2][l_column] or \
            grid_list[0][0] == grid_list[1][1] == grid_list[2][2] != ' ' or \
            grid_list[0][2] == grid_list[1][1] == grid_list[2][0] != ' ':
        return True
    return False

# function to handle button click
def button_click(row, col):
    global player_symbol, game_grid, move_counter, winner_flag, label

    # get button text and disable button
    button = buttons[row][col]
    if button['text'] != '':
        return
    button['text'] = player_symbol
    button['disabledforeground'] = 'black'

    # update grid and move counter
    game_grid[row][col] = player_symbol
    move_counter += 1

    # check for winner
    winner_flag = winner_check(game_grid, col, row)
    if winner_flag:
        label['text'] = f"Winner is PLAYER -= {player_symbol} =-"
        messagebox.showinfo("Winner", f"Winner is PLAYER -= {player_symbol} =-")
    elif move_counter == 9:
        label['text'] = "DRAW"
        messagebox.showinfo("Draw", "It's a draw!")
    else:
        player_symbol = "X" if move_counter % 2 == 0 else "O"
        label['text'] = f"PLAYER -= {player_symbol} =-"

# create Tkinter window and configure grid
window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry('250x300')
window.resizable(False, False)
window.grid_columnconfigure(0, minsize=80)
window.grid_columnconfigure(1, minsize=80)
window.grid_columnconfigure(2, minsize=80)
window.grid_rowconfigure(0, minsize=40)
window.grid_rowconfigure(1, minsize=40)
window.grid_rowconfigure(2, minsize=40)
window.grid_rowconfigure(3, minsize=40)

# create game grid and player symbol
game_grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player_symbol = "X"

# create buttons and label
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(window, text='', font=('Arial', 25), width=2, height=1,
                           command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i, column=j, sticky='news')
        row_buttons.append(button)
    buttons.append(row_buttons)
label = tk.Label(window, text=f"PLAYER -= {player_symbol} =-", font=('Arial', 12), width=15)
label.grid(row=3, columnspan=3)

# start game
move_counter = 0
winner_flag = False
window.mainloop()
