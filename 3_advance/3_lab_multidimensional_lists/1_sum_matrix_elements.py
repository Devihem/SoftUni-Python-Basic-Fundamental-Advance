rows, columns = input().split(", ")
new_matrix = [[int(x) for x in input().split(", ")] for _ in range(int(rows))]
max_sum = 0
for row in new_matrix:
    for number in row:
        max_sum += number

print(max_sum)
print(new_matrix)
