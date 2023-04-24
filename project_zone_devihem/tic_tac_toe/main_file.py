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
    # Print the game board grid in terminal for visualisation
    print(f"    {' | '.join(['1', '2', '3'])}"
          f"\n  • • • • • • •"
          f"\n1 • {' | '.join(grid_list[0])} •"
          f"\n  • {' + '.join(['—', '—', '—'])} •"
          f"\n2 • {' | '.join(grid_list[1])} •"
          f"\n  • {' + '.join(['—', '—', '—'])} •"
          f"\n3 • {' | '.join(grid_list[2])} •"
          f"\n  • • • • • • •")


def player_info(number_of_moves: int):
    # Set and Return player name and symbol.
    # Player One with [X] and Player Two with [O] based on the game current move.
    if number_of_moves % 2 == 1:
        p_symbol = "X"
        p_name = "Player One"
    else:
        p_symbol = "O"
        p_name = "Player Two"
    return p_symbol, p_name


def player_input():
    # After entering the input cast it to player_input_validator().
    # If input is correct it will return valid row and column otherwise will print Invalid.
    player_mark_place = input(f'\n     -= {player_name} =- '
                              f'\nPick where to place [{player_symbol}] mark!'
                              f'\n[row-column]:').split('-')

    row_valid, column_valid = player_input_validator(player_mark_place)
    return row_valid, column_valid


def player_input_validator(user_input: list):
    # Validating the input for Digits and Correct index.
    # ( using.isdigit and strip to eliminate negative numbers or other mistakes)
    if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit():
        # For correct index in the grid list - adding int(move)-1 for row and column
        row_index = int(user_input[0]) - 1
        column_index = int(user_input[1]) - 1
        if 0 <= column_index < 3 and 0 <= row_index < 3:
            if game_grid[row_index][column_index] == ' ':
                return row_index, column_index

    # If input is incorrect print - INVALID INPUT -
    print("\n• • • • • • • • •\n• INVALID INPUT •\n• • • • • • • • •\n")
    return player_input()


def end_game_print(board, pl_symbol, pl_name, flag_winner):
    terminal_visualisation(board)
    if flag_winner:
        print(f"\n• • • • • • • • • • •"
              f"\n•      WINNER       •"
              f"\n• {pl_name} — [{pl_symbol}]  •"
              f"\n• • • • • • • • • • •")
    else:
        print("\n• • • • • • • • •\n•  GAME — DRAW  •\n• • • • • • • • •\n")


# Starting_variable and board 3x3
winner_flag = False
moves = 0
player_symbol = ''
player_name = ''
max_moves = 9
game_grid = [[' ' for _ in range(3)] for _ in range(3)]

while not winner_flag and moves < max_moves:
    moves += 1

    # Returning the player in move -  Symbol and Name
    player_symbol, player_name = player_info(moves)

    # Printing the board in terminal
    terminal_visualisation(game_grid)

    # Player input and Validating the input if it's correct
    row, column = player_input()

    # Placing symbol in the grid
    game_grid[row][column] = player_symbol

    # Checking the grid for winner
    winner_flag = winner_check(game_grid, column, row)

end_game_print(game_grid, player_symbol, player_name, winner_flag)
