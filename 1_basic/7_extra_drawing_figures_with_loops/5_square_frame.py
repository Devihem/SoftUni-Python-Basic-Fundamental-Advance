size = int(input())
for i in range(1, size+1):
    for f in range(1, size+1):
        if (i == 1 and f == 1) or (i == size and f == 1) or (i == 1 and f == size) or (i == size and f == size):
            print("+", end=" ")
        elif (1 < i < size and f == 1) or (1 < i < size and f == size):
            print("|", end=" ")
        else:
            print("-", end=" ")
    print()
