m_row, m_col = map(int, input().split(','))
matrix = [list(input()) for _ in range(m_row)]
mao_r, mao_c = [(r, c) for c in range(m_col) for r in range(m_row) if matrix[r][c] == 'M'][0]

# Fast cheese detection:
cheese = 0
for row_cheese in matrix:
    for col_cheese in row_cheese:
        if col_cheese == 'C':
            cheese += 1

# Type 1 - 4 axis:
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# test zone
# # M C * @ T
# print(mao_r, mao_c)
# print(*matrix, sep="\n")

while True:

    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break

    r, c = directions[command]

    new_r = r + mao_r
    new_c = c + mao_c

    if 0 <= new_r < m_row and 0 <= new_c < m_col:
        if matrix[new_r][new_c] == '@':
            continue

        matrix[mao_r][mao_c] = '*'

        if matrix[new_r][new_c] == 'C':
            cheese -= 1

            # KISS
            matrix[new_r][new_c] = 'M'
            mao_r = new_r
            mao_c = new_c

            if cheese <= 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break

        elif matrix[new_r][new_c] == 'T':
            matrix[new_r][new_c] = 'M'
            print("Mouse is trapped!")
            break
        else:
            # KISS
            matrix[new_r][new_c] = 'M'
            mao_r = new_r
            mao_c = new_c
    else:
        print("No more cheese for tonight!")
        break

[print(''.join(row_print)) for row_print in matrix]
