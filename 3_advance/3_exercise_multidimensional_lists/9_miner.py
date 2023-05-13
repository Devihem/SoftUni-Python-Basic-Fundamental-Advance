def miner_location(maze:list):
    miner_location = \
        [[row, column] for column in range(len(maze)) for row in range(len(maze)) if matrix[row][column] == 's']
    m_row, m_column = miner_location[0]
    return m_row, m_column

matrix_size = int(input())
miner_moves = input().split()
matrix = [[x for x in input().split(' ')] for row in range(matrix_size)]

game_over_flag = False
collected_coals_flag = False

miner_row = 0
miner_column = 0
total_coal = 0

for move in miner_moves:

    miner_row, miner_column = miner_location(matrix)

    if move == 'up' and miner_row > 0:
        if matrix[miner_row - 1][miner_column] == 'e':
            game_over_flag = True

        matrix[miner_row][miner_column] = '*'
        matrix[miner_row - 1][miner_column] = 's'

    elif move == 'down' and miner_row < matrix_size - 1:
        if matrix[miner_row + 1][miner_column] == 'e':
            game_over_flag = True

        matrix[miner_row][miner_column] = '*'
        matrix[miner_row + 1][miner_column] = 's'

    elif move == 'left' and miner_column > 0:
        if matrix[miner_row][miner_column - 1] == 'e':
            game_over_flag = True

        matrix[miner_row][miner_column] = '*'
        matrix[miner_row][miner_column - 1] = 's'

    elif move == 'right' and miner_column < matrix_size - 1:
        if matrix[miner_row][miner_column + 1] == 'e':
            game_over_flag = True

        matrix[miner_row][miner_column] = '*'
        matrix[miner_row][miner_column + 1] = 's'

    total_coal = 0
    for row in matrix:
        for el in row:
            if el == 'c':
                total_coal += 1

    if total_coal == 0:
        collected_coals_flag = True

    if game_over_flag:
        break

    if collected_coals_flag:
        break


miner_row, miner_column = miner_location(matrix)
if game_over_flag:
    print(f"Game over! ({miner_row}, {miner_column})")
elif collected_coals_flag:
    print(f"You collected all coal! ({miner_row}, {miner_column})")
else:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_column})")

