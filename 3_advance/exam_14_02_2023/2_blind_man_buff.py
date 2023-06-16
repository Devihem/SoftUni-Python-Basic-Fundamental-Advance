matrix_rows , matrix_cols = map(int,input().split())

matrix = [input().split() for x in range(matrix_rows)]

man_r, man_c = [(r, c) for c in range(matrix_cols) for r in range(matrix_rows) if matrix[r][c] == 'B'][0]
matrix[man_r][man_c] = '-'

# Type 1 - 4 axis:
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

other_players = 3
moves = 0

while other_players > 0:

    command = input()
    if command == 'Finish':
        break
    dir_r, dir_c = directions[command]

    new_r = man_r + dir_r
    new_c = man_c + dir_c

    if 0 <= new_r < matrix_rows and 0 <= new_c < matrix_cols:
        if matrix[new_r][new_c] != 'O':
            if matrix[new_r][new_c] == 'P':
                other_players -= 1
            moves += 1
            man_r, man_c = new_r, new_c
print("Game over!")
print(f"Touched opponents: {3 - other_players} Moves made: {moves}")
