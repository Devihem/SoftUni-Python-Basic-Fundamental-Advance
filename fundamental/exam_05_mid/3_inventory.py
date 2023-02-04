inventory_list = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == "Craft!":
        break
    item = command[1]

    if command[0] == "Collect":
        if item not in inventory_list:
            inventory_list.append(item)
    elif command[0] == "Drop":
        if item in inventory_list:
            inventory_list.remove(item)
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(':')
        if old_item in inventory_list:
            old_item_index = inventory_list.index(old_item)
            inventory_list.insert(old_item_index +1, new_item)
    elif command[0] == "Renew":
        if item in inventory_list:
            inventory_list.append(item)
            inventory_list.remove(item)

print(*inventory_list, sep=", ")
