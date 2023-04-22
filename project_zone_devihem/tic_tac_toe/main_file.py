def winner_check(grid_list: list, l_column: int, l_row: int):
    # Checking for winner based on last move for row and column and specific for the diagonals.
    # Returning True or False statement
    if grid_list[l_row][0] == grid_list[l_row][1] == grid_list[l_row][2] or \
            grid_list[0][l_column] == grid_list[1][l_column] == grid_list[2][l_column] or \
            grid_list[0][0] == grid_list[1][1] == grid_list[2][2] != ' ' or \
            grid_list[0][2] == grid_list[1][1] == grid_list[2][0] != ' ':
        return True
    return False


def terminal_visualisation(grid_list: list):

    print(f"    {' | '.join(['1', '2', '3'])}"
          f"\n  • • • • • • •"
          f"\n1 • {' | '.join(grid_list[0])} •"
          f"\n  • {' + '.join(['—', '—', '—'])} •"
          f"\n2 • {' | '.join(grid_list[1])} •"
          f"\n  • {' + '.join(['—', '—', '—'])} •"
          f"\n3 • {' | '.join(grid_list[2])} •"
          f"\n  • • • • • • •")


# Starting_variable and board 3x3
winner_flag = False
move_counter = 0
player_symbol = ''
game_grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

while not winner_flag and move_counter < 9:
    move_counter += 1

    # Set Player - One with [X] and Player - Two with [O]
    if move_counter % 2 == 1:
        player_symbol = "X"
        player_name = "Player One"
    else:
        player_symbol = "O"
        player_name = "Player Two"

    # Printing the board in terminal
    terminal_visualisation(game_grid)

    # Validating the move, using .isdigit and strip to eliminate negative numbers or other mistakes.
    while True:
        player_move = input(f'\n     -= {player_name} =- \nPick where to place [{player_symbol}] mark!\n[row-column]:').split('-')
        if len(player_move) == 2 and player_move[0].isdigit() and player_move[1].isdigit():

            # For correct index in the grid list - adding int(move)-1
            row = int(player_move[0]) - 1
            column = int(player_move[1]) - 1
            if 0 <= column < 3 and 0 <= row < 3:
                if game_grid[row][column] == ' ':
                    break
        # If incorrect print - INVALID INPUT -
        print("\n• • • • • • • • •\n• INVALID INPUT •\n• • • • • • • • •\n")

    # Placing symbol in the grid
    game_grid[row][column] = player_symbol

    # Checking the grid for winner
    winner_flag = winner_check(game_grid, column, row)

terminal_visualisation(game_grid)
if winner_flag:
    print(f"\n\n Winner is PLAYER -= {player_symbol} =-")
else:
    print("\n• • • • • • • • •\n• GAME - DRAW  •\n• • • • • • • • •\n")
