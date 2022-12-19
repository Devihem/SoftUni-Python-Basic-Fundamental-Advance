n = int(input())

if n % 2 == 0:
    stars = 2
else:
    stars = 1

if n % 2 == 0:
    rows = n - 1
else:
    rows = n

for r1 in range(1, rows + 1):
    lines = int((n - stars) / 2)

    for l1 in range(0, lines):
        print("-", end="")
    if n % 2 == 1 and (r1 == 1 or r1 == rows):
        pass
    else:
        for l2 in range(lines+1, lines+2):
            print("*", end="")

    for l3 in range(lines+1, int((n+1)/2)):
        print("-", end="")

    for l4 in range(int((n+1)/2)+1, n-lines):
        print("-", end="")

    for l5 in range(((n - lines)-1),(n-lines)):
        print("*", end="")

    for l6 in range(n-lines, n):
        print("-", end="")

    if r1 < (rows/2):
        stars += 2
    else:
        stars -= 2
    print()
