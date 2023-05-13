matrix_row, matrix_column = map(int, input().split(' '))

matrix = [[element for element in input().split()] for _ in range(matrix_row)]

while True:

    new_command = input().split()
    if new_command[0] == 'END':
        break
    elif new_command[0] == 'swap':
        if len(new_command) == 5:
            for element in range(1, len(new_command), 2):
                if (int(new_command[element])) > matrix_row:
                    print("Invalid input!")
                    break
                elif (int(new_command[element + 1])) > matrix_column:
                    print("Invalid input!")
                    break
            else:
                matrix[int(new_command[1])][int(new_command[2])], matrix[int(new_command[3])][int(new_command[4])] = \
                matrix[int(new_command[3])][int(new_command[4])], matrix[int(new_command[1])][int(new_command[2])]
                [print(*row) for row in matrix]
        else:
            print("Invalid input!")
            continue
    else:
        print("Invalid input!")
        continue
