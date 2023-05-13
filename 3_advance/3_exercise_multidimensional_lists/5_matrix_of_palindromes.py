number_of_rows, number_of_columns = map(int, input().split(' '))

matrix = []

for row in range(number_of_rows):
    matrix.append([])
    for column in range(number_of_columns):
        matrix[row].append(f'{chr(row + 97)}{chr(row + column + 97)}{chr(row + 97)}')

[print(' '.join(row)) for row in matrix]
