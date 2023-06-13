map_size = int(input())
number_of_bombs = int(input())
directions = [
    # R , C   + Step  1 , -1 for dirrection
    (0, 1),  # Right - Left
    (1, 1),  # Prime Diagonal
    (1, 0),  # Down - Top
    (1, -1),  # Second Diagonal
]
map_matrix = [['0' for z in range(map_size)] for x in range(map_size)]
for bomb_number in range(number_of_bombs):
    bomb_r, bomb_c = input().strip('(').strip(')').split(', ')
    map_matrix[int(bomb_r)][int(bomb_c)] = '*'
    for step in [1, -1]:
        for dir_r, dir_c in directions:
            new_r = int(bomb_r) + dir_r * step
            new_c = int(bomb_c) + dir_c * step
            if 0 <= new_r < map_size and 0 <= new_c < map_size:
                if map_matrix[new_r][new_c] != '*':
                    map_matrix[new_r][new_c] = str(int(map_matrix[new_r][new_c]) + 1)

[print(' '.join(row)) for row in map_matrix]
