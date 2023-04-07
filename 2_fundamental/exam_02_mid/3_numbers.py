list_with_numbers = [int(number) for number in input().split()]
list_with_numbers.sort(reverse=True)
average_value = sum(list_with_numbers) / len(list_with_numbers)
final_list = []

for number in range(0, 5):
    if number in range(len(list_with_numbers)) and list_with_numbers[number] > average_value:
        final_list.append(list_with_numbers[number])

if len(final_list) == 0:
    print("No")
else:
    print(*final_list)
