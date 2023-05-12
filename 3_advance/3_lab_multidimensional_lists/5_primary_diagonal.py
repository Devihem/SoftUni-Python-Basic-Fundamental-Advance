number_of_rows = int(input())

matrix = [[row for row in input().split(' ')] for _ in range(number_of_rows)]
primary_diagonal_sum = 0
for row in range(len(matrix)):
    primary_diagonal_sum += int(matrix[row][row])

print(primary_diagonal_sum)