matrix_size = int(input())

matrix = [[x for x in input().split()] for _ in range(matrix_size)]

# All possible directions / vector
directions = (
    # (r , c)
    (-1, 0, 'up'),  # Up
    (1, 0, 'down'),  # Down
    (0, -1, 'left'),  # Left
    (0, 1, 'right'),  # right

)

maximum_eggs = 0
maximum_eggs_map = []
winning_direction = ""
bunny_r, bunny_c = (0, 0)

# Bunny location
for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == 'B':
            bunny_r, bunny_c = (row, col)

# Checking every direction
for direction_r, direction_c, name in directions:
    r, c = bunny_r, bunny_c
    current_direction_eggs = 0
    current_direction_eggs_map = []

    # While loop for the current direction
    while 0 <= r < matrix_size and 0 <= c < matrix_size:
        r += direction_r
        c += direction_c
        if 0 <= r < matrix_size and 0 <= c < matrix_size:
            if matrix[r][c] == 'X':
                break
            else:
                current_direction_eggs += int(matrix[r][c])
                current_direction_eggs_map.append([r, c])

    # Selecting the best path with maximum collected eggs
    if current_direction_eggs > maximum_eggs:
        maximum_eggs = current_direction_eggs
        maximum_eggs_map = current_direction_eggs_map
        winning_direction = name

# Final Print
if maximum_eggs > 0:
    print(winning_direction)
    print(*maximum_eggs_map, sep='\n')
    print(maximum_eggs)
