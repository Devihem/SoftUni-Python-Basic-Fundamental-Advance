max_load = float(input())
current_volume = max_load
counter = 0

while True:
    command = input()

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        command = float(command)

    counter += 1

    if counter % 3 == 0:
        command = command * 1.1

    if current_volume - command == 0:
        print("No more space!")
        break
    elif current_volume - command < 0:
        counter -= 1
        print("No more space!")
        break

    current_volume -= command

print(f"Statistic: {counter:.0f} suitcases loaded.")
