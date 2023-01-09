type_of_fire = input().split("#")
total_water = int(input())
effort = 0
total_fire_extinguished = 0
extinguished_cells = []
for fire in type_of_fire:
    fire = fire.split()
    if fire[0] == "High" and 81 <= int(fire[2]) <= 125:
        pass
    elif fire[0] == "Medium" and 51 <= int(fire[2]) <= 80:
        pass
    elif fire[0] == "Low" and 1 <= int(fire[2]) <= 50:
        pass
    else:
        continue
    fire_value = int(fire[2])
    if total_water >= fire_value:
        total_water -= fire_value
        effort += fire_value * 0.25
        total_fire_extinguished += fire_value
        extinguished_cells.append(fire[2])
print("Cells:", *extinguished_cells, sep="\n - ")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_extinguished}")
