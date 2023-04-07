x1_max = int(input())
x2_max = int(input())
x3_max = int(input())
prime_flag = True

for x1 in range(1, x1_max+1):
    if x1 % 2 == 1:
        continue
    for x2 in range(1, x2_max+1):
        if x2 < 2:
            continue
        elif 2 <= x2 <= 7:
            for i in range(2, int(x2 / 2)+1):
                if (x2 % i) == 0:
                    prime_flag = False
        else:
            continue
        if prime_flag == False:
            prime_flag = True
            continue
        for x3 in range(1, x3_max+1):
            if x3 % 2 == 1:
                continue
            print(f"{x1} {x2} {x3}")
