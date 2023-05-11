rows= input()
new_matrix = [[int(x)  if x % 2 == 0 else "" for x in input().split(", ")] for _ in range(int(rows))]
max_sum = 0
for row in new_matrix:
    for number in row:
        max_sum += number

print(max_sum)
print(new_matrix)
