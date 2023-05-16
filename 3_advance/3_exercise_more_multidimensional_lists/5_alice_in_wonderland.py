matrix_size = int(input())

matrix = [[x for x in input().split()] for _ in range(matrix_size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

# Add all move input in list while there is input


tea_bags_collected = 0

# Alice location
alice_r, alice_c = (0, 0)
for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice_r, alice_c = (row, col)

# Making the moves from the input r-row , c-column
while True:
    new_move = input()
    move_r, move_c = directions[new_move]
    new_r, new_c = move_r + alice_r, move_c + alice_c

    # Finding the next step and if it's on the matrix  (3 conditions to stop the loop 10-teabag,rabbit-h,out of map)
    if 0 <= new_r < matrix_size and 0 <= new_c < matrix_size:

        if matrix[new_r][new_c] == "R":
            matrix[new_r][new_c] = "*"
            print("Alice didn't make it to the tea party.")
            break  # 1 Alice hit a rabbit hole condition

        elif matrix[new_r][new_c] not in ('.', '*'):
            tea_bags_collected += int(matrix[new_r][new_c])

        matrix[new_r][new_c] = "*"
        alice_r, alice_c = new_r, new_c

    else:
        print("Alice didn't make it to the tea party.")
        break  # 2 Alice out of grid/matrix condition

    if tea_bags_collected >= 10:
        print("She did it! She went to the party.")
        break  # 3 Alice collected 10 tea_bags condition

[print(*row_print) for row_print in matrix]
