random_list = input().split(", ")
final_list = []

for item in random_list:
    current_word = ""
    for char in list(item):
        if char.isalnum() or char == "-" or char == "_":
            current_word += char
    if item == current_word:
        if 3 <= len(item) <= 16:
            final_list.append(item)

[print(f"{username}") for username in final_list]