number = int(input())
find_index = int(input())
bit_number = ""
counter = 0
while counter != 16:
    counter += 1
    bit_number = str(number % 2) + bit_number
    number = number // 2

print(bit_number[-(find_index+1)])