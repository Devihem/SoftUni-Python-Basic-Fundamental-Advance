numbers_list = [int(x) for x in input().split()]

numbers_to_be_removed = int(input())
working_number_list = sorted(numbers_list)
for removing in range(numbers_to_be_removed):
    working_number_list.pop(0)

for item in range(int(len(numbers_list)-1), -1, -1):
    current_value = numbers_list[item]
    if current_value not in working_number_list:
        numbers_list.pop(item)
print(str(numbers_list)[1:-1:])
