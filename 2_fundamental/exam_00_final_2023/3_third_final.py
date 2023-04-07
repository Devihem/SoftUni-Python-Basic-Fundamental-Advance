hero_dict = {}
while True:
    data_input = input().split(" ")

    command = data_input[0]

    if command == "End":
        break

    hero_name = data_input[1]
    if command == "Enroll":
        if hero_name not in hero_dict.keys():
            hero_dict[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif command == "Learn":
        hero_spell = data_input[2]
        if hero_name not in hero_dict.keys():
            print(f"{hero_name} doesn't exist.")
        else:
            if hero_spell in hero_dict[hero_name]:
                print(f"{hero_name} has already learnt {hero_spell}.")
            else:
                hero_dict[hero_name].append(hero_spell)

    elif command == "Unlearn":
        hero_unspell = data_input[2]
        if hero_name not in hero_dict.keys():
            print(f"{hero_name} doesn't exist.")
        else:
            if hero_unspell not in hero_dict[hero_name]:
                print(f"{hero_name} doesn't know {hero_unspell}.")
            else:
                hero_dict[hero_name].remove(hero_unspell)

print("Heroes:")
for hero in hero_dict.keys():
    hero_print_spells = ', '.join(hero_dict[hero])
    print(f"== {hero}: {hero_print_spells}")
