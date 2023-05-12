rows = int(input())

new_matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)]

print(new_matrix)
