plant_dictionary = {}
dictionary_input = int(input())

for data in range(dictionary_input):
    new_plant, rarity = input().split("<->")
    plant_dictionary[new_plant] = {rarity: []}

while True:

    command = input().split(": ")
    if command[0] == "Exhibition":
        break

    # Command Rate
    elif command[0] == "Rate":
        plant, rating = command[1].split(" - ")
        rarity_key = ""
        for r_key in plant_dictionary[plant].keys():
            rarity_key = r_key
        plant_dictionary[plant][rarity_key].append(rating)
        pass

    # Command Update
    elif command[0] == "Update":
        pass
    # Command Reset
    elif command[0] == "Reset":
        pass

print(plant_dictionary.items())