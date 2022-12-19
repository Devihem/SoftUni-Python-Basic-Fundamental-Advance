sample_number = int(input())
counter = 0

for i in range(1111, 9999+1):
    i = str(i)
    for x, y in enumerate(i):
        y = int(y)
        if y == 0:
            continue
        elif sample_number % y == 0:
            counter += 1
        if counter == 4:
            print(i, end=" ")
    counter = 0
