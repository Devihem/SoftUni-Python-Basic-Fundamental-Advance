class Peons:
    def __init__(self, nicknames):
        self.nicknames = nicknames


georgi = Peons("Rapidfire")
ivailo = Peons("Devihem")

print(georgi.nicknames)
georgi.hero = 'Demon'
print(georgi.__dict__)
print(ivailo.__dict__)