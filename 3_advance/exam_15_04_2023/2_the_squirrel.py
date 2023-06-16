matrix_size = int(input())
moves = input().split(', ')

matrix = [list(input()) for x in range(matrix_size)]

squ_r, squ_c = [(r, c) for c in range(matrix_size) for r in range(matrix_size) if matrix[r][c] == 's'][0]
hazelnuts = 0

# Type 1 - 4 axis:
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for move in moves:

    dir_r, dir_c = directions[move]

    new_r = squ_r + dir_r
    new_c = squ_c + dir_c

    if 0 <= new_r < matrix_size and 0 <= new_c < matrix_size:
        if matrix[new_r][new_c] == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            break

        if matrix[new_r][new_c] == 'h':
            hazelnuts += 1
            if hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                break
        matrix[new_r][new_c] = '*'
        squ_r, squ_c = new_r, new_c
    else:
        print("The squirrel is out of the field.")
        break
else:
    print("There are more hazelnuts to collect.")


print(f"Hazelnuts collected: {hazelnuts}")