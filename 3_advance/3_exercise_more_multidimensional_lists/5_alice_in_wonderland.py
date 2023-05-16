matrix_size = int(input())

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(matrix_size)]

print(*matrix,sep='\n')