class Vet:
    animals = []
    space = 5

    def __init__(self, name: str, ):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str):

        if Vet.space > 0:
            Vet.space -= 1
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"

        return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals:
            Vet.space += 1
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"

        return f"{animal_name} not in the clinic"

    def info(self):

        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")

print(peter.register_animal("Tom"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))

print(george.register_animal("Cory"))
print(george.register_animal("Kay"))

print(george.unregister_animal("Cory"))

print(peter.register_animal("Silky"))

print(peter.unregister_animal("Molly"))

print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
