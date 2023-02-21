travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for item in travel_route:
    item = item.split()
    command = item[0]

    if command == "Travel":
        distance = int(item[1])
        if fuel >= distance:
            print(f"The spaceship travelled {distance} light-years.")
            fuel -= distance
        else:
            print("Mission failed.")
            break

    elif command == "Enemy":
        enemy_armour = int(item[1])
        if enemy_armour <= ammunition:
            print(f"An enemy with {enemy_armour} armour is defeated.")
            ammunition -= enemy_armour
        else:
            if fuel >= enemy_armour * 2:
                fuel -= enemy_armour * 2
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif command == "Repair":
        ammunition_fuel_added = int(item[1])
        fuel += ammunition_fuel_added
        ammunition += ammunition_fuel_added * 2
        print(f"Ammunitions added: {ammunition_fuel_added * 2}.")
        print(f"Fuel added: {ammunition_fuel_added}.")
    elif command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
