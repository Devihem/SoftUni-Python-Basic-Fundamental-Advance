matrix_size = int(input())
matrix = [[int(x) for x in input().split(' ')] for row in range(matrix_size)]
bombs_list = [[int(coordinate) for coordinate in info.split(',')] for info in input().split()]

move_directions = (
    (-1, 0),  # UP
    (1, 0),  # DOWN
    (0, -1),  # LEFT
    (0, 1),  # RIGHT
    (-1, -1),  # UP-LEFT
    (-1, 1),  # UP-RIGHT
    (1, -1),  # DOWN-LEFT
    (1, 1),  # DOWN-RIGHT
    (0, 0),  # CENTER
)

alive_cell = 0
total_sum = 0

for row_bomb, column_bomb in bombs_list:
    current_bomb_dmg = matrix[row_bomb][column_bomb]
    if current_bomb_dmg < 1:
        continue
    for x, y in move_directions:
        current_row, current_col = row_bomb + x, column_bomb + y

        if 0 <= current_row < matrix_size and 0 <= current_col < matrix_size:
            matrix[current_row][current_col] -= current_bomb_dmg if matrix[current_row][current_col] > 0 else 0

alive_cell = [num for row_cell in matrix for num in row_cell if int(num > 0)]

print(f'Alive cells: {len(alive_cell)}')
print(f'Sum: {sum(alive_cell)}')
[print(*row_print) for row_print in matrix]
