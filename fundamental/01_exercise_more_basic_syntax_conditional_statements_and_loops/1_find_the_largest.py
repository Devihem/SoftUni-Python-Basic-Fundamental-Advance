random_number = input()

list_test = []

for x in random_number:
    list_test.append(int(x))
    list_test.sort(reverse=True)

for y in list_test:
    print(y, end="")
