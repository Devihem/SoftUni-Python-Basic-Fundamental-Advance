num = int(input())
reversed_num = 0

while num != 0:
    curr_digit = num % 10
    reversed_num = 10 * reversed_num
    reversed_num = reversed_num + curr_digit
    num = num // 10

first_number = int((repr(reversed_num)[0]))
second_number = int((repr(reversed_num)[1]))
third_number = int((repr(reversed_num)[2]))

for x1 in range(1, first_number + 1):
    for x2 in range(1, second_number + 1):
        for x3 in range(1, third_number + 1):
            print(f"{x1} * {x2} * {x3} = {x1*x2*x3};")
