matrix_size = int(input())

matrix = [list(input()) for _ in range(matrix_size)]

knight_movement = (
    # (R , C)
    (-1, -2),  # Up-Left 1
    (-2, -1),  # Up-Left 2
    (-1, 2),  # Up-Right 1
    (-2, 1),  # Up-Right 2
    (1, -2),  # Down-Left 1
    (2, -1),  # Down-Left 2
    (1, 2),  # Down-Right 1
    (2, 1),  # Down-Right 2
)

knight_removed_count = 0
knight_most_targets = 0
knight_r, knight_c = (0, 0)

while True:

    # The matrix is square NxN
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == 'K':
                knight_most_targets_current = 0
                for r, c in knight_movement:

                    if 0 <= r + row < matrix_size and 0 <= c + col < matrix_size:
                        if matrix[r + row][c + col] == 'K':
                            knight_most_targets_current += 1
                else:
                    if knight_most_targets_current > knight_most_targets:
                        knight_most_targets = knight_most_targets_current
                        knight_r, knight_c = (row, col)
    else:
        if knight_most_targets > 0:
            matrix[knight_r][knight_c] = '0'
            knight_removed_count += 1
            knight_r, knight_c = (0, 0)

    # Going through the matrix checking K one by one for this with most targets

    if knight_most_targets == 0:
        break
    knight_most_targets = 0

print(knight_removed_count)
