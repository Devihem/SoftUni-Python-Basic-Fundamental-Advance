route = input().split("||")
fuel = int(input())
ammo = int(input())

for item in route:
    item = item.split(" ")
    command = item[0]

    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    value = int(item[1])
    if command == "Travel":
        distance = value
        if fuel >= distance:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break

    elif command == "Enemy":
        enemy_hp = value
        if ammo >= enemy_hp:
            ammo -= enemy_hp
            print(f"An enemy with {enemy_hp} armour is defeated.")
        else:
            if fuel >= enemy_hp * 2:
                fuel -= enemy_hp * 2
                print(f"An enemy with {enemy_hp} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif command == "Repair":
        repair = value
        ammo += repair * 2
        fuel += repair
        print(f"Ammunitions added: {repair*2}.")
        print(f"Fuel added: {repair}.")

