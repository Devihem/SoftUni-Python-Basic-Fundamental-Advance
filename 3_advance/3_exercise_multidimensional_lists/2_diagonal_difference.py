matrix_size = int(input())

matrix = [[int(x) for x in input().split(' ')] for row in range(matrix_size)]

primary_diagonal = []
secondary_diagonal = []

for row in range(matrix_size):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][-row-1])

primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)

print(abs(primary_diagonal_sum-secondary_diagonal_sum))