x1_range = int(input())
x2_range = int(input())
x3_range = int(input())
flag_not_prime = False

for x1 in range(1, x1_range+1):
    if x1 % 2 == 1:
        continue
    for x2 in range(1, x2_range + 1):
        if x2 == 1:
            continue
        elif 2 <= x2 <= 7:
            for x2_prime in range(2, int(x2/2)+1):
                if x2 % x2_prime == 0:
                    flag_not_prime = True
        else:
            continue
        if flag_not_prime:
            flag_not_prime = False
            continue

        for x3 in range(1, x3_range + 1):
            if x3 % 2 == 1:
                continue
            else:
                print(x1, x2, x3)
