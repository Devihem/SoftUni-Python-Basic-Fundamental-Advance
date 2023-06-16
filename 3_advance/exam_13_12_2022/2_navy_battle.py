matrix_size = int(input())
map_matrix = [list(input()) for x in range(matrix_size)]
sub_r, sub_c = [(r, c) for c in range(matrix_size) for r in range(matrix_size) if map_matrix[r][c] == 'S'][0]

# Type 1 - 4 axis:
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# - * C S
total_ships, total_hp = 3, 3

while total_ships > 0 and total_hp > 0:
    map_matrix[sub_r][sub_c] = '-'

    direction = input()

    new_r, new_c = directions[direction]

    sub_r += new_r
    sub_c += new_c

    if map_matrix[sub_r][sub_c] == '*':
        total_hp -= 1

    elif map_matrix[sub_r][sub_c] == 'C':
        total_ships -= 1

    map_matrix[sub_r][sub_c] = 'S'

if total_ships == 0:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{sub_r}, {sub_c}]!")

[print(''.join(x)) for x in map_matrix]