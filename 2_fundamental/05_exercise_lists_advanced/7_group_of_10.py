list_of_number = input().split(", ")
all_lists = []
working_group = 0
working_list = list_of_number.copy()
while len(list_of_number) >= 1:
    working_group += 10
    all_lists += [[]]
    for index_number in range(len(list_of_number)):

        int_number = int(list_of_number[index_number])

        if int_number <= working_group:
            all_lists[working_group//10 - 1].append(list_of_number[index_number])
            working_list.remove(list_of_number[index_number])
    else:
        list_of_number = working_list.copy()

for group in range(len(all_lists)):
    all_lists[group] = [int(number) for number in all_lists[group]]
    print(f"Group of {(group+1) * 10}'s: {all_lists[group]}")
