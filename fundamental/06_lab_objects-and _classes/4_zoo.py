class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species: str, name: str):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {''.join(self.mammals)}\nTotal animals:{zoo.__animals}"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {''.join(self.fishes)}\nTotal animals:{zoo.__animals}"
        elif species == "bird":
            result += f"Birds in {self.zoo_name}: {''.join(self.birds)}\nTotal animals:{zoo.__animals}"
        return result


zoo_name_input = input()
zoo = Zoo(zoo_name_input)

animals_count = int(input())

for animal in range(animals_count):
    species_input, name_input = (input().split())
    zoo.add_animal(species_input, name_input)

info_about_this_species_input = input()
print(zoo.get_info(info_about_this_species_input))
