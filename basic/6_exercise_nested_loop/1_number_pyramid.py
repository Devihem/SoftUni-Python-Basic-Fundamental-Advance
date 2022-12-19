n = int(input())
number = 0
for i in range(1, n):
    if number > n:
        break
    for f in range(1, i):
        number += 1
        if number > n:
            break
        print(number, end="")
    print()
