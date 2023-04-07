grocery_list = input().split(" ")
searched_items_list = input().split(" ")
grocery_dict = {}

for food_index in range(0, len(grocery_list), 2):
    grocery_dict[grocery_list[food_index]] = int(grocery_list[food_index + 1])

for searched_item in searched_items_list:
    if searched_item in grocery_dict:
        print(f"We have {grocery_dict[searched_item]} of {searched_item} left")
    else:
        print(f"Sorry, we don't have {searched_item}")
