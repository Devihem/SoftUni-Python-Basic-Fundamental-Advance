matrix_size = int(input())

matrix = [[int(x) for x in input().split(' ')] for row in range(matrix_size)]

primary_diagonal = []
secondary_diagonal = []

for row in range(matrix_size):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][-row-1])

print(f"Primary diagonal: {' '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {' '.join([str(y) for y in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")