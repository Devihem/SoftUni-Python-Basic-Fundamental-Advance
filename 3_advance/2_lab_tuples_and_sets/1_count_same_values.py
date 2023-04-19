new_input = [float(x) for x in input().split()]
new_set = {float(new_number) for new_number in new_input}
new_dict = {number: new_input.count(number) for number in new_set}
[print(f'{key} - {new_dict[key]} times') for key in new_dict.keys()]
