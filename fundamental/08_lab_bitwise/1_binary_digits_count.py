number = int(input())
check_for_one_zero = int(input())
bit_number = ""
while number != 0:
    bit_number = str(number % 2) + bit_number
    number = number // 2
counter = 0
for item in list(bit_number):
    if int(item) == check_for_one_zero:
        counter += 1
print(counter)
