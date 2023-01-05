numbers_count = int(input())
positive_number_list = []
negative_number_list = []
for new_number_input in range(0, numbers_count):
    new_number = int(input())
    if new_number > 0:
        positive_number_list.append(new_number)
    else:
        negative_number_list.append(new_number)

print(positive_number_list)
print(negative_number_list)
print(f"Count of positives: {len(positive_number_list)}")
print(f"Sum of negatives: {sum(negative_number_list)}")
