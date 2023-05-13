matrix_size = int(input())
matrix = [[int(x) for x in input().split(' ')] for row in range(matrix_size)]
bombs_list = [x.split(',') for x in input().split()]
total_sum = 0
alive_cell = 0

for row_bomb, column_bomb in bombs_list:
    current_bomb_dmg = matrix[int(row_bomb)][int(column_bomb)]
    if current_bomb_dmg < 1:
        continue
    # first_box_with_the_bomb - hp = 0
    matrix[int(row_bomb)][int(column_bomb)] = 0

    # HARD CODE
    row_bomb = int(row_bomb)
    column_bomb = int(column_bomb)
    # 1
    try:
        if matrix[int(row_bomb)-1][int(column_bomb)-1] > 0 and row_bomb >= 1 and column_bomb >= 1:
            matrix[int(row_bomb)-1][int(column_bomb)-1] -= current_bomb_dmg
    except IndexError:
        pass

    # 2
    try:
        if matrix[int(row_bomb) - 1][int(column_bomb)] > 0 and row_bomb >= 1 and column_bomb >= 0:
            matrix[int(row_bomb) - 1][int(column_bomb)] -= current_bomb_dmg
    except IndexError:
        pass

    # 3
    try:
        if matrix[int(row_bomb) - 1][int(column_bomb) + 1] > 0 and row_bomb >= 1 and column_bomb < matrix_size - 1:
            matrix[int(row_bomb) - 1][int(column_bomb) + 1] -= current_bomb_dmg
    except IndexError:
        pass

    # 4
    try:
        if matrix[int(row_bomb)][int(column_bomb) - 1] > 0 and row_bomb >= 0 and column_bomb >= 1:
            matrix[int(row_bomb)][int(column_bomb) - 1] -= current_bomb_dmg
    except IndexError:
        pass

    # 6
    try:
        if matrix[int(row_bomb)][int(column_bomb) + 1] > 0 and row_bomb >= 0 and column_bomb < matrix_size - 1:
            matrix[int(row_bomb)][int(column_bomb) + 1] -= current_bomb_dmg
    except IndexError:
        pass

    # 7
    try:
        if matrix[int(row_bomb) + 1][int(column_bomb) - 1] > 0 and row_bomb < matrix_size - 1 and column_bomb >= 1:
            matrix[int(row_bomb) + 1][int(column_bomb) - 1] -= current_bomb_dmg
    except IndexError:
        pass

    # 8
    try:
        if matrix[int(row_bomb) + 1][int(column_bomb)] > 0 and row_bomb < matrix_size - 1 and column_bomb >= 0:
            matrix[int(row_bomb) + 1][int(column_bomb)] -= current_bomb_dmg
    except IndexError:
        pass

    # 9
    try:
        if matrix[int(row_bomb) + 1][int(column_bomb) + 1] > 0 and row_bomb < matrix_size - 1 and column_bomb < matrix_size - 1:
            matrix[int(row_bomb) + 1][int(column_bomb) + 1] -= current_bomb_dmg
    except IndexError:
        pass

for row_cell in matrix:
    for el in row_cell:
        if int(el) > 0:
            alive_cell += 1
            total_sum += int(el)

print(f'Alive cells: {alive_cell}')
print(f'Sum: {total_sum}')
[print(*row_print) for row_print in matrix]