first_number = int(input())
last_number = int(input())

for x1 in range(first_number, last_number+1):
    pass
    for x2 in range(first_number, last_number + 1):
        pass
        for x3 in range(first_number, last_number + 1):
            pass
            for x4 in range(first_number, last_number + 1):
                if x1 > x4:
                    if (x2+x3) % 2 == 0:
                        if (x1 % 2 == 0 and x4 % 2 == 1) or (x4 % 2 == 0 and x1 % 2 == 1):
                            print(f"{x1}{x2}{x3}{x4}", end=" ")
