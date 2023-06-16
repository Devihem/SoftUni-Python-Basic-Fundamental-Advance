SIZE = 6

MAPP = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)

}

matrix = [input().split() for _ in range(SIZE)]
x, y = map(int, input().strip('(').strip(')').split(', '))
current_position = int(matrix[x][y]) if matrix[x][y].isdigit() else matrix[x][y]

while True:
    data = input().split()
    if data[0] == 'Stop':
        break
    command = data[0]
    direction = data[1]
    print(direction)
    print(MAPP[direction])
    dx, dy = MAPP[direction]
    x += dx
    y += dy
    current_position = matrix[x][y]

    if command == 'Create':
        if matrix[x][y] == '.':
            matrix[x][y] = data[2]

    elif command == 'Update':
        if matrix[x][y].isalpha() or matrix[x][y].isdigit():
            matrix[x][y] = data[2]

    elif command == 'Delete':
        if matrix[x][y].isalpha() or matrix[x][y].isdigit():
            matrix[x][y] = '.'

    elif command == 'Read':
        if matrix[x][y].isalpha() or matrix[x][y].isdigit():
            print(matrix[x][y])

for i in matrix:
    print(*matrix)