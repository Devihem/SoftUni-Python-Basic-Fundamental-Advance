words_dict = {}
for x in range(0, int(input())):
    key = input()
    value = input()
    if key not in words_dict:
        words_dict[key] = value
    else:
        words_dict[key] += f", {value}"

[print(f"{item} - {words_dict[item]}") for item in words_dict]