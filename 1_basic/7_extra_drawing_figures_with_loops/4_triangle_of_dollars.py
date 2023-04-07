size = int(input())

for i in range(0, size):
    for f in range(0, size):
        if i < f:
            break
        print("$", end=" ",)
    print()
