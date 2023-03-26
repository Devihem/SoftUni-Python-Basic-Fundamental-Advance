plant_rarity_dictionary = {}
plant_rating_dictionary = {}
dictionary_input = int(input())

for data in range(dictionary_input):
    new_plant, rarity = input().split("<->")
    plant_rarity_dictionary[new_plant] = rarity
    plant_rating_dictionary[new_plant] = []

while True:

    command = input().split(": ")
    if command[0] == "Exhibition":
        break

    info_given = command[1].split(" - ")
    plant = info_given[0]

    if plant not in plant_rarity_dictionary:
        print("error")

    # Command Rate
    elif command[0] == "Rate":
        rating = info_given[1]
        plant_rating_dictionary[plant].append(int(rating))

    # Command Update
    elif command[0] == "Update":
        new_rarity = info_given[1]
        plant_rarity_dictionary[plant] = new_rarity

    # Command Reset
    elif command[0] == "Reset":
        plant_rating_dictionary[plant] = []

for plant in plant_rating_dictionary.keys():
    total_rating = sum(plant_rating_dictionary[plant])
    if total_rating > 0:
        average_rating = total_rating / len(plant_rating_dictionary[plant])
    else:
        average_rating = total_rating
    plant_rating_dictionary[plant] = average_rating

print("Plants for the exhibition:")
for plant_print in plant_rarity_dictionary.keys():
    print(f"- {plant_print};"
          f" Rarity: {plant_rarity_dictionary[plant_print]};"
          f" Rating: {plant_rating_dictionary[plant_print]:.2f}")
