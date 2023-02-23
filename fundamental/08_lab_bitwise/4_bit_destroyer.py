number = int(input())
find_index = int(input())
bit_number = ""
counter = 0
while counter != 16:
    counter += 1
    bit_number = str(number % 2) + bit_number
    number = number // 2
lst = list(bit_number)
lst[15 - find_index] = 0

lst = list(reversed(lst))
final_sum = 0
for index, item in enumerate(lst):
    if int(item) == 1:
        final_sum += 2 ** index
print(final_sum)
