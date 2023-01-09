day_events_list = input().split("|")
energy = 100
coins = 100

for event in day_events_list:
    event = event.split("-")
    current_event = event[0]
    points = int(event[1])
    if current_event == "rest":
        if energy + points <= 100:
            energy += points
            print(f"You gained {points} energy.")
        else:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        print(f"Current energy: {energy}.")

    elif current_event == "order":
        if energy >= 30:
            coins += points
            energy -= 30
            print(f"You earned {points} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")

    else:
        if points <= coins:
            coins -= points
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
