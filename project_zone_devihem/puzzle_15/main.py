import random

# puzzle solving pattern
pattern_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

# Create a puzzle and then randomly place each number.
puzzle_grid = [number for number in range(16)]
puzzle_grid = [[puzzle_grid.pop(random.randint(0, len(puzzle_grid) - 1)) for _ in range(4)] for _ in range(4)]

# statring values
zero_row = 0
zero_column = 0
while puzzle_grid != pattern_grid:

    print(*puzzle_grid, sep='\n')
    user_input = input('\nWASD --->:')

    # FINDING ZERO ( mapping ? )
    for row in range(4):
        for column in range(4):
            if puzzle_grid[row][column] == 0:
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
    print("Ta da da")
    print(*puzzle_grid, sep='\n')