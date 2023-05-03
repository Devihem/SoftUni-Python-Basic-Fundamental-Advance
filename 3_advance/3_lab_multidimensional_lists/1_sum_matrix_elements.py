rows, columns = input().split(", ")
new_matrix = [input().split(", ") for _ in range(int(rows))]
max_sum = 0
for row in new_matrix:
    for number in row:
        max_sum += int(number)

print(max_sum)
print(new_matrix)
