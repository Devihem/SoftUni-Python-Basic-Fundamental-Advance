m_size = int(input())
racer_name = input()
matrix = [input().split() for x in range(m_size)]
car_r, car_c = 0,0
total_km = 0

# Type 1 - 4 axis:
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:

    command = input()
    if command == 'End':
        matrix[car_r][car_c] = 'C'
        print(f"Racing car {racer_name} DNF.")
        break


    new_r, new_c = directions[command]
    car_r += new_r
    car_c += new_c

    if matrix[car_r][car_c] == '.':
        total_km += 10
        continue
    elif matrix[car_r][car_c] == 'F':
        total_km += 10
        matrix[car_r][car_c] = 'C'
        print(f"Racing car {racer_name} finished the stage!")
        break
    elif matrix[car_r][car_c] == 'T':
        matrix[car_r][car_c] = '.'
        total_km += 30
        car_r, car_c = [(row, col) for col in range(m_size) for row in range(m_size) if matrix[row][col] == 'T'][0]
        matrix[car_r][car_c] = '.'

print(f"Distance covered {total_km} km." )
[print(''.join(x)) for x in matrix]
# Finding UNIT place:
# row_r, row_c = [(row, col)
#                 for col in range(matrix_size)
#                 for row in range(matrix_size) if map_matrix[row][col] == 'SYMBOL'][0]
