number_loop = int(input())

for number in range(1, number_loop+1):
    digit = number
    digit_sum = 0
    while digit > 0:
        digit_sum += digit % 10
        digit = int(digit/10)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
