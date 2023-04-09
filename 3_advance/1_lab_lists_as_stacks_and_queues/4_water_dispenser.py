water_dispenser_litters = int(input())
queue_list = []

while True:
    command_or_name = input()
    if command_or_name == "Start":
        break
    queue_list.append(command_or_name)

while True:
    command = input().split()
    if command[0] == "End":
        print(f"{water_dispenser_litters} liters left")
        break
    elif command[0] == "refill":
        refill_quantity = int(command[1])
        water_dispenser_litters += refill_quantity
    else:
        wanted_quantity_water = int(command[0])
        person_name = ''.join(queue_list[:1])
        queue_list = queue_list[1:]
        if water_dispenser_litters >= wanted_quantity_water:
            water_dispenser_litters -= wanted_quantity_water
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
