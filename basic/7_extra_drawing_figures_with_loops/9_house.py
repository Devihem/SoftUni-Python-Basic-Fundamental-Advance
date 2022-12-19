from math import floor
n = int(input())

lines = 0
if n % 2 == 0:
    stars = 2
else:
    stars = 1

z = (floor((n+1)/2)+1)

for rows_a in range(1, z):
    lines = (n - stars) / 2
    lines = int(lines)
    for l1 in range(0, lines):
        print("-", end="")
    for l2 in range(lines+1, (n - lines)+1):
        print("*", end="")
    for l3 in range(lines+stars, n):
        print("-", end="")

    stars += 2
    print()

for rows_b in range(1, (floor(n/2) + 1)):
    for x2 in range(1, n+1):
        if x2 == 1 or x2 == n:
            print("|", end="")
        else:
            print("*", end="")
    print()
