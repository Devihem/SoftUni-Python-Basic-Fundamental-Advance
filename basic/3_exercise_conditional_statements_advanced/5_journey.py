budget = float(input())
season = input()

place = ""
destination = ""
vacation_money = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_money = budget*0.30
        place = "Camp"
    elif season == "winter":
        vacation_money = budget*0.70
        place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_money = budget*0.40
        place = "Camp"
    elif season == "winter":
        vacation_money = budget*0.80
        place = "Hotel"
elif budget > 1000:
    destination = "Europe"
    vacation_money = budget*0.90
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {vacation_money:.2f}")
