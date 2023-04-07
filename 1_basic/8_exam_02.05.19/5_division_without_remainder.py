number_loop = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(0, number_loop):
    number = int(input())

    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

print(f"{p1 / number_loop * 100:.2f}%")
print(f"{p2 / number_loop * 100:.2f}%")
print(f"{p3 / number_loop * 100:.2f}%")