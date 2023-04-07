numbers_list = input().split(", ")
for number_index in range(int(len(numbers_list) - 1), -1, -1):
    if int(numbers_list[number_index]) == 0:
        numbers_list.pop(number_index)
        numbers_list.append("0")

print("[", end="")
print(*numbers_list, sep=", ", end="")
print("]")
