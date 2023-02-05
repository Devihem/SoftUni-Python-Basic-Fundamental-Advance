def command_shoot_e_3_3(list_with_targets: list, index_target: int, shot_power: int):
    if index_target in range(len(list_with_targets)):
        list_with_targets[index_target] -= shot_power
        if list_with_targets[index_target] <= 0:
            list_with_targets.pop(index_target)
    return list_with_targets


def command_add_e_3_3(list_with_targets: list, index_insert: int, target_health: int):
    if index_insert in range(len(list_with_targets)):
        targets_list.insert(index_insert, target_health)
    else:
        print("Invalid placement!")
    return list_with_targets


def command_strike_e_3_3(list_with_targets: list, strike_index: int, radius: int):
    if strike_index - radius >= 0 and strike_index + radius < len(list_with_targets):
        list_with_targets = list_with_targets[:strike_index - radius] + list_with_targets[strike_index + radius + 1:]
    else:
        print("Strike missed!")
    return list_with_targets


targets_list = list(map(int, input().split()))
while True:

    system_input = input()
    if system_input == "End":
        targets_list = [str(value) for value in targets_list]
        print('|'.join(targets_list))
        break

    command, index, value = system_input.split()

    if command == "Shoot":
        targets_list = command_shoot_e_3_3(targets_list, int(index), int(value))
    elif command == "Add":
        targets_list = command_add_e_3_3(targets_list, int(index), int(value))
    elif command == "Strike":
        targets_list = command_strike_e_3_3(targets_list, int(index), int(value))