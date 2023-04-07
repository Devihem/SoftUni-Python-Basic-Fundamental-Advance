number = int(input())
bit_number = ""
counter = 0
while counter != 8:
    counter += 1
    bit_number = str(number % 2) + bit_number
    number = number // 2

bit_number = bit_number[-8:]
print(bit_number[6])
