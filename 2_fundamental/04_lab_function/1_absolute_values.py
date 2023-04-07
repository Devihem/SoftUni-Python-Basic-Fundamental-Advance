list_with_numbers = input().split()
reworked_list = []
for number in list_with_numbers:
    number = float(number)
    reworked_list.append(abs(number))
print(reworked_list)
abs()