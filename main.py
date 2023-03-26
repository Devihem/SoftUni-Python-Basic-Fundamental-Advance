class Plant:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.ratings = []

    def rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0


plants = {}

n = int(input())
for num in range(n):
    token = input().split('<->')
    plant_name = token[0]
    plant_rarity = token[1]
    plants[plant_name] = Plant(plant_name, int(plant_rarity))

command = input()
while command != 'Exhibition':
    token_2 = command.split(': ')
    token_3 = token_2[1].split(' - ')
    plant_name = token_3[0]
    command_type = token_2[0]

    if plant_name not in plants:
        print('error')

    elif command_type == 'Rate':
        rating = token_3[1]
        plants[plant_name].ratings.append(int(rating))

    elif command_type == 'Update':
        new_rarity = int(token_3[1])
        plants[plant_name].rarity = new_rarity

    elif command_type == 'Reset':
        plants[plant_name].ratings.clear()

    else:
        print('error')

    command = input()

sorted_plants = sorted(plants.values(), key=lambda p: (p.rarity, p.rating()), reverse=True)

print(f'Plants for the exhibition:')
for plant in sorted_plants:
    print(f'- {plant.name}; Rarity: {plant.rarity}; Rating: {plant.rating():.2f}')