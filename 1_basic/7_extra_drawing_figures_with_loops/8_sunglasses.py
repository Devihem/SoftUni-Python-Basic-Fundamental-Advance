n = int(input())
if n % 2 == 0:
    middle_part = n/2
else:
    middle_part = (n+1) / 2

if 3 <= n <= 100:
    for row in range(1, n+1):

        for x1 in range(1, n*2+1):
            if row == 1 or row == n:
                print("*", end="")
            elif row != 1 and row != n:
                if x1 == 1 or x1 == n*2:
                    print("*", end="")
                else:
                    print("/", end="")

        for x2 in range(0, n):
            if row == middle_part:
                print("|", end="")
            else:
                print(" ", end="")

        for x1 in range(1, n * 2 + 1):
            if row == 1 or row == n:
                print("*", end="")
            elif row != 1 and row != n:
                if x1 == 1 or x1 == n * 2:
                    print("*", end="")
                else:
                    print("/", end="")
        print()
