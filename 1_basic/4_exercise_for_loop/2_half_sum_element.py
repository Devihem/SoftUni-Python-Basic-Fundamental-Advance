from sys import maxsize

loop = int(input())

total = 0
max = -maxsize

for i in range(0, loop):
    x = int(input())
    total += x
    if max < x:
        max = x

if total-max == max:
    print("Yes")
    print("Sum =", (max))
elif total-max != max:
    print("No")
    print("Diff =", (abs((total-max)-max)))
