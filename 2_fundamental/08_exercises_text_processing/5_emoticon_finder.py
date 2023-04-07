random_str = input()
list_split = list(random_str)
index = 0
for char in list_split:
    if char == ":":
        print(char + list_split[index + 1])
    index += 1
