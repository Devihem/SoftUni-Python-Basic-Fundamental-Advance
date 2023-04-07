budget = float(input())
season = input()

place = 0

if budget <= 1000:
    house_type = "Camp"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    house_type = "Hut"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.60

elif budget > 3000:
    house_type = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        place = "Alaska"
    elif season == "Winter":
        place = "Morocco"

print(f"{place} - {house_type} - {price:.2f}")
