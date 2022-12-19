num = input()

first_number = int(num[2])
second_number = int(num[1])
third_number = int(num[0])

for x1 in range(1, first_number + 1):
    for x2 in range(1, second_number + 1):
        for x3 in range(1, third_number + 1):
            print(f"{x1} * {x2} * {x3} = {x1*x2*x3};")
