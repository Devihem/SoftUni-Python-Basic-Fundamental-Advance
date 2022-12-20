number_of_iteration = int(input())
tank_max_capacity = 255
tank_current_capacity = 0
for iteration in range(number_of_iteration):
    new_liters_of_waters = int(input())
    if tank_current_capacity + new_liters_of_waters > tank_max_capacity:
        print("Insufficient capacity!")
        continue
    else:
        tank_current_capacity += new_liters_of_waters
print(tank_current_capacity)
