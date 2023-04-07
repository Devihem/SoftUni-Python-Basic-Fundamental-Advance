dungeon_rooms = input().split("|")
health = 100
bitcoins = 0

for room in dungeon_rooms:
    command, value = room.split()

    if command == "potion":
        heal = int(value)
        if health + heal <= 100:
            health += heal
            print(f"You healed for {heal} hp.")
        else:
            print(f"You healed for {100 - health} hp.")
            health = 100
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += int(value)
        print(f"You found {value} bitcoins.")

    else:
        monster = command
        health -= int(value)
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {dungeon_rooms.index(room)+1}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
