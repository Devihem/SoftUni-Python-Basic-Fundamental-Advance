import random


def create_random_puzzle_board():
    # Create a puzzle and then randomly place each number.
    created_puzzle_board = [str(number) if len(str(number)) == 2 else ' ' + str(number) for number in range(16)]
    # Empty box symbol
    created_puzzle_board[0] = ' □'
    # Using random.randint for unique board every game
    created_puzzle_board = [
        [created_puzzle_board.pop(random.randint(0, len(created_puzzle_board) - 1)) for _ in range(4)] for _ in
        range(4)]
    return created_puzzle_board


def printing_the_board(puzzle_board: list):
    # Visual representation of the board in terminal
    print(f'\n\n\n\n╔═════╦═════╦═════╦═════╗'
          f'\n║ {"  ║ ".join(puzzle_board[0])}  ║'
          f'\n╠═════╬═════╬═════╬═════╣'
          f'\n║ {"  ║ ".join(puzzle_board[1])}  ║'
          f'\n╠═════╬═════╬═════╬═════╣'
          f'\n║ {"  ║ ".join(puzzle_board[2])}  ║'
          f'\n╠═════╬═════╬═════╬═════╣'
          f'\n║ {"  ║ ".join(puzzle_board[3])}  ║'
          f'\n╚═════╩═════╩═════╩═════╝')


def user_input_and_control():
    # Show the "Game Control" and returning the input
    player_input = input('\n      ╔═════╗      ╔══════╗'
                         '\n      ║  W↑ ║      ║ Enter║ '
                         '\n╔═════╬═════╬═════╗╚══╗   ║'
                         '\n║  ←A ║  S↓ ║  D→ ║   ║   ║'
                         '\n╚═════╩═════╩═════╝   ╚═══╝'
                         '\nKey + Enter -> :')
    return player_input.upper()


# Create the board and randomly place the blocks using .randint
puzzle_grid = create_random_puzzle_board()

# puzzle solving pattern
pattern_grid = [[' 1', ' 2', ' 3', ' 4'], [' 5', ' 6', ' 7', ' 8'], [' 9', '10', '11', '12'], ['13', '14', '15', ' □']]
# staring variables
zero_row = 0
zero_column = 0

while puzzle_grid != pattern_grid:

    # Printing the current stage of the game ( the board )
    printing_the_board(puzzle_grid)

    # Accepting the user input and showing the control
    user_input = user_input_and_control()

    # FINDING ZERO ( mapping ? )
    for row in range(4):
        for column in range(4):
            if puzzle_grid[row][column] == ' □':
                zero_row = row
                zero_column = column

    # UP
    if user_input == 'W' and zero_row > 0:
        puzzle_grid[zero_row][zero_column], puzzle_grid[zero_row - 1][zero_column] \
            = puzzle_grid[zero_row - 1][zero_column], puzzle_grid[zero_row][zero_column]

        # DOWN
    elif user_input == 'S' and zero_row < 3:
        puzzle_grid[zero_row][zero_column], puzzle_grid[zero_row + 1][zero_column] \
            = puzzle_grid[zero_row + 1][zero_column], puzzle_grid[zero_row][zero_column]
    # LEFT
    elif user_input == 'A' and zero_column > 0:
        puzzle_grid[zero_row][zero_column], puzzle_grid[zero_row][zero_column - 1] \
            = puzzle_grid[zero_row][zero_column - 1], puzzle_grid[zero_row][zero_column]
        # LEFT
    # RIGHT
    elif user_input == 'D' and zero_column < 3:
        puzzle_grid[zero_row][zero_column], puzzle_grid[zero_row][zero_column + 1] \
            = puzzle_grid[zero_row][zero_column + 1], puzzle_grid[zero_row][zero_column]
        # LEFT

else:
    print("WINNERRR")
    print(printing_the_board(puzzle_grid))
