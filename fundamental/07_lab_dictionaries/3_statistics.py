grocery_dict = {}
while True:

    system_info = input()
    if system_info == "statistics":
        print(f"Products in stock:")
        [print(f"- {key}: {value}") for (key, value) in grocery_dict.items()]
        print(f"Total Products: {len(grocery_dict)}")
        print(f"Total Quantity: {sum(grocery_dict.values())}")
        break
    else:
        system_info = system_info.split(": ")
        if system_info[0] in grocery_dict:
            grocery_dict[system_info[0]] += int(system_info[1])
        else:
            grocery_dict[system_info[0]] = int(system_info[1])
