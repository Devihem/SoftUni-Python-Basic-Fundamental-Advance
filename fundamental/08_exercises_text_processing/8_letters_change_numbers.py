string_list = input().split()
final_sum = 0

for item in string_list:
    current_number = int(item[1: len(item)-1])
    current_value_first_letter = ord(item[0].upper()) - 64
    current_value_last_letter = ord(item[-1].upper()) - 64

    if item[0].isupper():
        current_number /= current_value_first_letter
    elif item[0].islower():
        current_number *= current_value_first_letter

    if item[-1].isupper():
        current_number -= current_value_last_letter
    elif item[-1].islower():
        current_number += current_value_last_letter

    final_sum += current_number
print(f"{final_sum:.2f}")
