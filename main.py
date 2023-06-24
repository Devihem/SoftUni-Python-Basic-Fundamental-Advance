class Peons:
    special_list = []
    def __init__(self, nicknames):
        self.nicknames = nicknames

    def __str__(self):
        return self.nicknames

georgi = Peons("Rapidfire")
ivailo = Peons("Devihem")
print(georgi.nicknames)
georgi.hero = 'Demon'

Peons.special_list.append(georgi)
Peons.special_list.append(ivailo)
print(Peons.special_list)


print(georgi)