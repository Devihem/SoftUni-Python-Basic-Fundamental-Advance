matrix_size = 6
planet_matrix = [input().split() for _ in range(matrix_size)]
commands_list = input().split(', ')

row_r, row_c = [(row, col) for col in range(6) for row in range(6) if planet_matrix[row][col] == 'E'][0]

colony_items = {
    'W': 0,
    'M': 0,
    'C': 0,
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for command in commands_list:

    planet_matrix[row_r][row_c] = '-'
    dir_r, dir_c = directions[command]

    # new place R
    row_r += dir_r
    if row_r < 0:
        row_r = matrix_size - 1
    elif row_r > matrix_size - 1:
        row_r = 0

    # new place C
    row_c += dir_c
    if row_c < 0:
        row_c = matrix_size - 1
    elif row_c > matrix_size - 1:
        row_c = 0

    if planet_matrix[row_r][row_c] == 'R':
        print(f"Rover got broken at ({row_r}, {row_c})")
        break
    elif planet_matrix[row_r][row_c] != '-':
        colony_items[planet_matrix[row_r][row_c]] += 1
        material = planet_matrix[row_r][row_c]

        if material == "W":
            material = 'Water deposit'
        elif material == "M":
            material = 'Metal deposit'
        elif material == "C":
            material = 'Concrete deposit'
        print(f"{material} found at ({row_r}, {row_c})")

    planet_matrix[row_r][row_c] = "E"

if all([True if x > 0 else False for x in colony_items.values()]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
