new_items = input()
working_list = new_items.split(" ")
reformated_working_list = []

for item in working_list:
    opposite_number = int(item) * (-1)
    reformated_working_list.append(opposite_number)

print(reformated_working_list)
