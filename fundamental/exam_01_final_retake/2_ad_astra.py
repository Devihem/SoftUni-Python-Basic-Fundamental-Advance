import re

food_text_input = input()
energy_kcal_per_day = 2000
total_kcal = 0
food_list = []

# ReGex
food_finder_pattern = r"[#]([a-zA-Z]+[\s]*[a-zA-Z]*)#([\d]{2}\/[\d]{2}\/[\d]{2})#(\d+)#|" \
                      r"[\|]([a-zA-Z]+\s*[a-zA-Z]*)[\|]([\d]{2}\/[\d]{2}\/[\d]{2})[\|](\d+)[\|]"
food_info_match = re.findall(food_finder_pattern, food_text_input)

for food in food_info_match:
    current_list = []
    for data in food:
        if data != "":
            current_list.append(data)
    food_list.append(current_list)

for item in food_list:
    item_kcal = int(item[2])
    total_kcal += item_kcal

print(f"You have food to last you for: {total_kcal//energy_kcal_per_day} days!")
[print(f"Item: {info_item[0]}, Best before: {info_item[1]}, Nutrition: {info_item[2]}") for info_item in food_list]
