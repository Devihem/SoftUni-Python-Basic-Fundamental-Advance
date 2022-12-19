first_num = int(input())
second_num = int(input())
bonus_first_num = int(input())
bonus_second_num = int(input())

for x1 in range(first_num, first_num + bonus_first_num + 1):
    for x1_prime in range(2, x1):
        if (x1 % x1_prime) == 0:
            break
    else:
        for x2 in range(second_num, second_num + bonus_second_num + 1):
            for x2_prime in range(2, x2):
                if x2 % x2_prime == 0:
                    break
            else:
                print(f"{x1}{x2}")
