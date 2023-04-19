new_input = [float(x) for x in input().split()]
new_dict = {}

for number in new_input:
    if number not in new_dict.keys():
        new_dict[number] = 0
    new_dict[number] += 1

[print(f"{key} - {new_dict[key]} times") for key in new_dict.keys()]
