divisor = int(input())
boundary_number = int(input())
max_multiple_numb = 0
x1 = 0

for x1 in range(boundary_number, divisor-1, -1):

    if (x1 % divisor == 0) and x1 <= boundary_number:
        max_multiple_numb = x1
        break

if x1 > 0:
    print(max_multiple_numb)
