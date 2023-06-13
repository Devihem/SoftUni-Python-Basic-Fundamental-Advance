board = [input().split() for _ in range(8)]

king_row = 0
king_col = 0
queens_in_check = []

directions = [
    (-1, 0),  # UP
    (1, 0),  # DOWN
    (0, -1),  # LEFT
    (0, 1),  # RIGHT
    (1, 1),  # PRIME D-R
    (-1, -1),  # PRIME U-L
    (1, -1),  # SECONDARY D-L
    (-1, 1),  # SECONDARY U-R
]
for row in range(8):
    for col in range(8):
        if board[row][col] == 'K':
            king_row = row
            king_col = col

for dir_r, dir_c in directions:
    for steps in range(8):
        new_r = king_row + dir_r * steps
        new_c = king_col + dir_c * steps
        if 0 <= new_r < 8 and 0 <= new_c < 8:
            if board[new_r][new_c] == 'Q':
                queens_in_check.append([new_r, new_c])
                break

if len(queens_in_check) > 0:
    [print(x) for x in queens_in_check]
else:
    print("The king is safe!")
