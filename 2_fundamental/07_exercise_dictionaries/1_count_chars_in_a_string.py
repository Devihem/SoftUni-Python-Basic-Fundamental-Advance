char_list = list(input())
char_dict = {}
for item in char_list:
    if item != " ":
        if item not in char_dict:
            char_dict[item] = 1
        else:
            char_dict[item] += 1

[print(f"{key} -> {char_dict[key]}") for key in char_dict]
