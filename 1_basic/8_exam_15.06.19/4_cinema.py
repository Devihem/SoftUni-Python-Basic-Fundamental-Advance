seats = int(input())
people_coming = input()
income = 0
used_seats = 0
while True:
    people_coming = int(people_coming)

    if used_seats + people_coming > seats:
        print("The cinema is full.")
        break
    used_seats += people_coming
    if people_coming % 3 == 0:
        income += people_coming * 5 - 5
    else:
        income += people_coming * 5
    people_coming = input()

    if people_coming == "Movie time!":
        print(f"There are {seats - used_seats} seats left in the cinema.")
        break

    elif used_seats <= 0:
        print("The cinema is full.")
        break

print(f"Cinema income - {income} lv.")
