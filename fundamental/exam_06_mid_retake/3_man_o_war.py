def command_fire_6_3(ship_status: list, atk_index: int, atk_damage: int):
    if atk_index in range(len(ship_status)):
        ship_status[atk_index] -= atk_damage
    return ship_status


def command_defend_6_3(ship_status: list, starting_index: int, ending_index: int, atk_damage: int):
    if starting_index >= 0 and ending_index < len(ship_status):
        for sector_index, value in enumerate(ship_status):
            if sector_index in range(starting_index, ending_index + 1):
                ship_status[sector_index] -= atk_damage
    return ship_status


def command_repair_6_3(ship_status: list, repair_index: int, restored_health: int, max_health: int):
    if repair_index in range(len(ship_status)):
        ship_status[repair_index] += restored_health
        if ship_status[repair_index] > max_health:
            ship_status[repair_index] = max_health
    return ship_status


def command_status_6_3(ship_status: list, max_health: int):
    sections = 0
    for item in ship_status:
        if item < max_health * 0.2:
            sections += 1
    return sections


def ship_structure_validator(ship_status: list):
    for value in ship_status:
        if value <= 0:
            return True
    return False


pirate_ship = [int(number) for number in input().split(">")]
warship_ship = [int(number) for number in input().split(">")]
maximum_hp = int(input())
pirate_ship_sink_flag = False
warship_ship_sink_flag = False

while True:

    system_input = input().split()
    command = system_input[0]
    if command == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(warship_ship)}")
        break

    elif command == "Fire":
        index = int(system_input[1])
        pirate_damage = int(system_input[2])
        warship_ship = command_fire_6_3(warship_ship, index, pirate_damage)
        warship_ship_sink_flag = ship_structure_validator(warship_ship)
        if warship_ship_sink_flag:
            print("You won! The enemy ship has sunken.")
            break

    elif command == "Defend":
        start_index = int(system_input[1])
        end_index = int(system_input[2])
        warship_damage = int(system_input[3])
        pirate_ship = command_defend_6_3(pirate_ship, start_index, end_index, warship_damage)
        pirate_ship_sink_flag = ship_structure_validator(pirate_ship)
        if pirate_ship_sink_flag:
            print("You lost! The pirate ship has sunken.")
            break

    elif command == "Repair":
        repair_place = int(system_input[1])
        health = int(system_input[2])
        pirate_ship = command_repair_6_3(pirate_ship, repair_place, health, maximum_hp)

    elif command == "Status":
        section_needed_repair = command_status_6_3(pirate_ship, maximum_hp)
        print(f"{section_needed_repair} sections need repair.")
