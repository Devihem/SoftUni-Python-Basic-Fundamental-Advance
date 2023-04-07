number_of_lines = int(input())
number_list = []
formatted_list = []

for new_number in range(0, number_of_lines):
    new_number_input = int(input())
    number_list.append(new_number_input)

format_command = input()
for item in number_list:
    if format_command == "even":
        if item % 2 == 0:
            formatted_list.append(item)
    elif format_command == "odd":
        if item % 2 == 1:
            formatted_list.append(item)
    elif format_command == "positive":
        if item >= 0:
            formatted_list.append(item)
    elif format_command == "negative":
        if item < 0:
            formatted_list.append(item)

print(formatted_list)
