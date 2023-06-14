string_in_list = list(input())
matrix_size = int(input())
matrix = [list(input()) for _ in range(matrix_size)]
for_loop_moves = int(input())
player_loc = [(row, col) for col in range(matrix_size) for row in range(matrix_size) if matrix[row][col] == 'P']
player_r, player_c = player_loc[0]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for _ in range(for_loop_moves):

    direction_name = input()

    new_r, new_c = directions[direction_name]

    new_player_r = player_r + new_r
    new_player_c = player_c + new_c

    if 0 <= new_player_r < matrix_size and 0 <= new_player_c < matrix_size:
        matrix[player_r][player_c] = '-'
        if matrix[new_player_r][new_player_c] != '-':
            string_in_list.append(matrix[new_player_r][new_player_c])
        matrix[new_player_r][new_player_c] = 'P'

        player_r = new_player_r
        player_c = new_player_c

    else:
        if string_in_list:
            string_in_list.pop()

print(*string_in_list, sep='')
[print(''.join(row_print)) for row_print in matrix]
