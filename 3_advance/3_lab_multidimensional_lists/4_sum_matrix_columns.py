number_of_rows, number_of_columns = map(int, input().split(', '))

matrix = [[row for row in input().split(' ')] for _ in range(number_of_rows)]

for column in range(len(matrix[0])):
    column_sum = 0
    for row in matrix:
        column_sum += int(row[column])
    print(column_sum)