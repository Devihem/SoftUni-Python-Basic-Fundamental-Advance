class Heroes:
    DEFAULT_MAIN_WEAPON = ['Sword', 'Shield']

    def __init__(self, nicknames):
        self.nicknames = nicknames
        self._gold = 0

    def __str__(self):
        return f"{self.nicknames} have {self._gold} gold"


class Pets:
    def __init__(self, pet_type, name, health, speed):
        self.pet_type = pet_type
        self.name = name
        self.health = health
        self.speed = speed

    def info(self):
        return f"-=[ {self.name} - {self.pet_type} ]=-  \nThis pet is with {self.health} HP. Base move speed is {self.speed}"


class Dragons(Pets):
    def __init__(self, pet_type, name, health, speed,wings_type):
        super().__init__(pet_type, name, health, speed)
        self.wings_type = wings_type
    def dragon_text(self):
        return f"I'm {self.name} a {self.pet_type} from a very far land !"

    def dragon_flex(self):
        return f"Flex with {self.wings_type}"

class Wolfs(Pets):
    pass


georgi = Heroes("Rapidfire")
ivailo = Heroes("Devihem")
dragon_1 = Dragons("Dragon", "Balthazar", 1200, 120, "Iron - Feathers")
wolf_1 = Wolfs("Wolf", "Fenrir", 300, 150)

print(dragon_1.info())
print(wolf_1.info())
print(dragon_1.dragon_text())
print(dragon_1.dragon_flex())