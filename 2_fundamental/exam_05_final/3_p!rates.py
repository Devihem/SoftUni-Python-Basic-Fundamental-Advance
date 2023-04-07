city_population_dict = {}
city_gold_dict = {}


while True:
    city_info = input()
    if city_info == "Sail":
        break
    city, population, gold = city_info.split("||")

    if city in city_population_dict:
        city_population_dict[city] = int(population) + city_population_dict[city]
        city_gold_dict[city] = int(gold) + city_gold_dict[city]
    else:
        city_population_dict[city] = int(population)
        city_gold_dict[city] = int(gold)

while True:

    attack_info = input().split("=>")
    if attack_info[0] == "End":
        break

    # Command - PLUNDER
    elif attack_info[0] == "Plunder":
        attacked_town = attack_info[1]
        attacked_people = attack_info[2]
        attacked_gold = attack_info[3]
        print(f"{attacked_town} plundered! {attacked_gold} gold stolen, {attacked_people} citizens killed.")
        city_population_dict[attacked_town] = city_population_dict[attacked_town] - int(attacked_people)
        city_gold_dict[attacked_town] = city_gold_dict[attacked_town] - int(attacked_gold)
        if city_population_dict[attacked_town] == 0 or city_gold_dict[attacked_town] == 0:
            city_population_dict.pop(attacked_town)
            city_gold_dict.pop(attacked_town)
            print(f"{attacked_town} has been wiped off the map!")

    # Command - PROSPER
    elif attack_info[0] == "Prosper":
        prosper_town = attack_info[1]
        prosper_gold = int(attack_info[2])
        if prosper_gold >= 0:
            city_gold_dict[prosper_town] = city_gold_dict[prosper_town] + prosper_gold
            print(f"{prosper_gold} gold added to the city treasury. {prosper_town} now has {city_gold_dict[prosper_town]} gold.")
        else:
            print("Gold added cannot be a negative number!")

if len(city_population_dict) > 0:
    print(f"Ahoy, Captain! There are {len(city_population_dict)} wealthy settlements to go to:")
    [print(f"{city} -> Population: {city_population_dict[city]} citizens, Gold: {city_gold_dict[city]} kg")
     for city in city_population_dict.keys()]
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
