from collections import  deque

substrings = deque(input().split())

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

founded_colors = []
while substrings:

    first_symbols = substrings.popleft()
    if substrings:
        second_symbol = substrings.pop()
    else:
        second_symbol = ''

    created_string_1 = first_symbols + second_symbol
    created_string_2 = second_symbol + first_symbols

    if created_string_1 in main_colors:
        founded_colors.append(created_string_1)
    elif created_string_2 in main_colors:
        founded_colors.append(created_string_2)
    elif created_string_1 in secondary_colors:
        founded_colors.append(created_string_1)
    elif created_string_2 in secondary_colors:
        founded_colors.append(created_string_2)
    else:
        # if len(substrings) > 1:
        split_index = (len(substrings)-1)//2
        new_list = [first_symbols[:-1], second_symbol[:-1]]
        substrings = list(substrings)
        substrings = substrings[0:split_index+1] + new_list + substrings[split_index+1:]
        substrings = deque([x for x in substrings if x != ''])

final_color_list = []
for color in founded_colors:
    if color in ['orange', 'purple', 'green']:
        if color == 'orange' and 'red' in founded_colors and 'yellow' in founded_colors:
            final_color_list.append(color)
        elif color == 'purple' and 'red' in founded_colors and 'blue' in founded_colors:
            final_color_list.append(color)
        if color == 'green' and 'blue' in founded_colors and 'yellow' in founded_colors:
            final_color_list.append(color)
    else:
        final_color_list.append(color)

print(final_color_list)
