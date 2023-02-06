def command_urgent_4_2(item_list: list, urgent_item: str):
    if urgent_item not in item_list:
        item_list.insert(0, urgent_item)
    return item_list


def command_unnecessary_4_2(item_list: list, unnecessary_item: str):
    if unnecessary_item in item_list:
        item_list.remove(unnecessary_item)
    return item_list


def command_correct_4_2(item_list: list, old_item: str, replacing_item: str):
    if old_item in item_list:
        replace_index = item_list.index(old_item)
        item_list[replace_index] = replacing_item
    return item_list


def command_rearrange_4_2(item_list: list, rearrange_item: str):
    if rearrange_item in item_list:
        item_list.remove(rearrange_item)
        item_list.append(rearrange_item)
    return item_list


shopping_list = input().split('!')

while True:

    system_input = input()

    if system_input == "Go Shopping!":
        break
    system_input = system_input.split()
    command = system_input[0]
    item = system_input[1]

    if command == "Urgent":
        shopping_list = command_urgent_4_2(shopping_list, item)

    elif command == "Unnecessary":
        shopping_list = command_unnecessary_4_2(shopping_list, item)

    elif command == "Correct":
        new_item = system_input[2]
        shopping_list = command_correct_4_2(shopping_list, item, new_item)

    elif command == "Rearrange":
        shopping_list = command_rearrange_4_2(shopping_list, item)

print(*shopping_list, sep=', ')
