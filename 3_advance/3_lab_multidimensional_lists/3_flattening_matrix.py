number_of_rows = int(input())

matrix = [[row for row in input().split(', ')] for _ in range(number_of_rows)]
flatten_matrix = [int(element) for row in matrix for element in row]
print(flatten_matrix)
