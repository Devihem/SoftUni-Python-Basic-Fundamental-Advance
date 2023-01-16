digits_input = input().split(" ")
base_chars_list = list(input())
digits_reformated_list = []
coded_message = []
for number_index in digits_input:
    if int(number_index) < 0:
        continue
    new_sum = 0
    for digit in number_index:
        new_sum += int(digit)
    digits_reformated_list.append(new_sum)

if base_chars_list:
    for value in digits_reformated_list:
        while value >= len(base_chars_list):
            value -= len(base_chars_list)
        coded_message.append(base_chars_list[value])
        base_chars_list.pop(value)

print(*coded_message, sep="")
