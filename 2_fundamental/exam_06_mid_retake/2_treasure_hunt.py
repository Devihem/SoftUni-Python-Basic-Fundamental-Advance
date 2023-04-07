def command_loot_6_2(treasure_chest: list, new_looted_treasures: list):
    new_looted_treasures = [item for item in new_looted_treasures if item not in treasure_chest]
    treasure_chest = list(reversed(new_looted_treasures)) + treasure_chest_list
    return treasure_chest


def command_drop_6_2(treasure_chest: list, chest_drop_index: int):
    if chest_drop_index in range(len(treasure_chest)):
        treasure_chest.append(treasure_chest.pop(chest_drop_index))
    return treasure_chest


def command_steal_6_2(treasure_chest: list, steal_count: int):
    steal_items_index = (len(treasure_chest) - steal_count)
    if steal_items_index < 0:
        steal_items_index = 0
    steal_items_list = treasure_chest[steal_items_index:]
    treasure_chest = treasure_chest[:steal_items_index]
    print(', '.join(steal_items_list))
    return treasure_chest


treasure_chest_list = input().split("|")

while True:
    system_input = input().split()
    command = system_input[0]
    if command == "Yohoho!":
        break
    elif command == "Loot":
        loot_treasure_list = system_input
        loot_treasure_list.remove("Loot")
        treasure_chest_list = command_loot_6_2(treasure_chest_list, loot_treasure_list)
    elif command == "Drop":
        drop_index = int(system_input[1])
        treasure_chest_list = command_drop_6_2(treasure_chest_list, drop_index)
    elif command == "Steal":
        steal_index = int(system_input[1])
        treasure_chest_list = command_steal_6_2(treasure_chest_list, steal_index)

treasure_sum = sum([len(item) for item in treasure_chest_list])
if treasure_sum <= 0:
    print("Failed treasure hunt.")
else:
    average_treasure = treasure_sum / len(treasure_chest_list)
    print(f"Average treasure gain: {average_treasure:.2f} pirate credits.")
