fuel_type = input()
fuel_in_tank = int(input())




if fuel_type in ["Diesel","Gasoline","Gas"]:
    if fuel_in_tank >= 25:
         print(f"You have enough {fuel_type.lower()}.")

    elif fuel_in_tank < 25:
         print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")