def dragon_stats_def(dragon_input: str):
    # dragon info - input + checking for null data
    drag_type, drag_name, drag_dmg, drag_hp, drag_armor = dragon_input.split()
    if drag_dmg == "null":
        drag_dmg = 45
    if drag_hp == "null":
        drag_hp = 250
    if drag_armor == "null":
        drag_armor = 10
    return drag_type, drag_name, int(drag_dmg), int(drag_hp), int(drag_armor)


number_of_dragons = int(input())
dragon_dict = {}

for dragon in range(number_of_dragons):
    dragon_info = input()
    d_type, name, dmg, health, armor = dragon_stats_def(dragon_info)

    if d_type not in dragon_dict.keys():
        dragon_dict[d_type] = {}
    if name not in dragon_dict[d_type].keys():
        dragon_dict[d_type][name] = 0
    dragon_dict[d_type][name] = [dmg, health, armor]

for dragon_type in dragon_dict:
    dragon_names_sorted = sorted(dragon_dict[dragon_type].keys())

    # average stats process
    avr_dmg, avr_hp, avr_armor = 0, 0, 0
    avr_len = len(dragon_dict[dragon_type].keys())
    for stats in dragon_dict[dragon_type].values():
        avr_dmg += stats[0]
        avr_hp += stats[1]
        avr_armor += stats[2]
    avr_dmg, avr_hp, avr_armor = avr_dmg/avr_len, avr_hp/avr_len, avr_armor/avr_len

    # dragons type + average stats
    print(f"{dragon_type}::({avr_dmg:.2f}/{avr_hp:.2f}/{avr_armor:.2f})")

    # dragons names print + personal stats
    [print(f"-{dragon_name} ->"
           f" damage: {dragon_dict[dragon_type][dragon_name][0]},"
           f" health: {dragon_dict[dragon_type][dragon_name][1]},"
           f" armor: {dragon_dict[dragon_type][dragon_name][2]}")
     for dragon_name in dragon_names_sorted]
