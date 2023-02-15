phone_reg_dict = {}

while True:

    system_input = input()
    if system_input.isdigit():
        searched_index = int(system_input)
        break
    else:
        name, number = system_input.split("-")
    phone_reg_dict[name] = number

for searched_name in range(0, searched_index):
    searching = input()
    if searching not in phone_reg_dict:
        print(f"Contact {searching} does not exist.")
    else:
        print(f"{searching} -> {phone_reg_dict[searching]}")
