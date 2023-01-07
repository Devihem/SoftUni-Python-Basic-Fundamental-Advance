items_for_shuffle = input()
number_of_shuffles = int(input())
items_list = items_for_shuffle.split(" ")
shuffle_list_a = []
shuffle_list_b = []

for shuffle in range(1, number_of_shuffles+1):
    shuffle_list_a = items_list[:int(len(items_list)/2)]
    shuffle_list_b = items_list[int(len(items_list)/2):]
    items_list = []
    for item in range(int(len(shuffle_list_a))):
        items_list.append(shuffle_list_a[item])
        items_list.append(shuffle_list_b[item])

print(items_list)
