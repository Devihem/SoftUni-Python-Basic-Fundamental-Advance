starter_loop = int(input())

if 1 <= starter_loop <= 100:

    for row in range(0, starter_loop+1):
        for f1 in range(0, starter_loop - row):
            print(" ", end="")
        for f2 in range(0, row):
            print("*", end="")

        print(" | ", end="")

        for f3 in range(0, row):
            print("*", end="")
        for f4 in range(0, starter_loop - row):
            print(" ", end="")

        print()
