bakery_list = input().split(" ")
bakery_dict = {}
for food_index in range(0, len(bakery_list), 2):
    bakery_dict[bakery_list[food_index]] = int(bakery_list[food_index+1])
print(bakery_dict)
