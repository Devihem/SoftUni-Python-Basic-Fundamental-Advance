def merging_list_indexes_5_9(item_list: list, start_index: int, end_index: int):
    if start_index >= len(item_list):
        start_index = len(item_list) - 1
    elif start_index < 0:
        start_index = 0
    if end_index >= len(item_list) - 1:
        end_index = len(item_list) - 1
    item_list[start_index:end_index + 1] = ["".join(item_list[start_index:end_index + 1])]
    return item_list


def divide_list_cell_5_9(item_list: list, divided_index: int, partitions: int):
    segments_in_cell = len(item_list[divided_index])
    max_item_in_cell = segments_in_cell // partitions
    if partitions > len(item_list[divided_index]):
        max_item_in_cell = 1
    new_list_reformated = [""]
    working_index = 0
    for symbol in item_list[divided_index]:
        if len(new_list_reformated) == partitions:
            new_list_reformated[working_index] += symbol
            continue
        if len(new_list_reformated[working_index]) == max_item_in_cell:
            new_list_reformated += [""]
        if len(new_list_reformated[working_index]) == max_item_in_cell:
            working_index += 1

        new_list_reformated[working_index] += symbol
    item_list.pop(divided_index)

    for index, value in enumerate(new_list_reformated):
        item_list.insert(divided_index + index, value)
    return item_list


message_code_list = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        message_code_list = merging_list_indexes_5_9(message_code_list, int(command[1]), int(command[2]))
    elif command[0] == "divide":
        message_code_list = divide_list_cell_5_9(message_code_list, int(command[1]), int(command[2]))

print(" ".join(message_code_list))
