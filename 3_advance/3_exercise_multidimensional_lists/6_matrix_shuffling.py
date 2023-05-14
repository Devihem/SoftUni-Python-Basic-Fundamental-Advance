matrix_row, matrix_column = map(int, input().split(' '))

matrix = [[element for element in input().split()] for _ in range(matrix_row)]

while True:

    new_command = input().split()
    if new_command[0] == 'END':
        break
    elif new_command[0] == 'swap':
        if len(new_command) == 5:
            if int(new_command[1]) < matrix_row and int(new_command[2]) < matrix_column and \
                    int(new_command[3]) < matrix_row and int(new_command[4]) < matrix_column:
                matrix[int(new_command[1])][int(new_command[2])], matrix[int(new_command[3])][int(new_command[4])] = \
                    matrix[int(new_command[3])][int(new_command[4])], matrix[int(new_command[1])][int(new_command[2])]
                [print(*row) for row in matrix]
            else:
                print("Invalid input!")
                continue
        else:
            print("Invalid input!")
            continue
    else:
        print("Invalid input!")
        continue
