number_of_cars = int(input())
cars_mileage = {}
cars_fuel = {}
for new_car in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars_mileage[car] = int(mileage)
    cars_fuel[car] = int(fuel)

while True:

    command = input().split(" : ")
    if command[0] == "Stop":
        break

    # Command DRIVE
    elif command[0] == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars_fuel[car] >= fuel:
            cars_mileage[car] = cars_mileage[car] + distance
            cars_fuel[car] = cars_fuel[car] - fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_mileage[car] >= 100000:
                cars_mileage.pop(car)
                cars_fuel.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    # Command REFUEL
    elif command[0] == "Refuel":
        car, refuel = command[1], int(command[2])
        car_current_fuel = cars_fuel[car]
        if car_current_fuel + refuel <= 75:
            cars_fuel[car] = car_current_fuel + refuel
            print(f"{car} refueled with {refuel} liters")
        else:
            cars_fuel[car] = 75
            print(f"{car} refueled with {75 - car_current_fuel} liters")

    # Command REVERT
    elif command[0] == "Revert":
        car, mileage = command[1], int(command[2])
        car_current_mileage = cars_mileage[car]
        if car_current_mileage - mileage >= 10000:
            cars_mileage[car] = car_current_mileage - mileage
            print(f"{car} mileage decreased by {mileage} kilometers")
        else:
            cars_mileage[car] = 10000

[print(f"{car} -> Mileage: {cars_mileage[car]} kms, Fuel in the tank: {cars_fuel[car]} lt.")
    for car in cars_mileage.keys()]
