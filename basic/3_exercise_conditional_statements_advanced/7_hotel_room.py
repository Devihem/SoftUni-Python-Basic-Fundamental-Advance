month = input()
days = int(input())

studio = 0
studio_bonus = 1
apartment = 0
apartment_bonus = 1

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < days <= 14:
        studio_bonus = 0.95
    elif days > 14:
        studio_bonus = 0.70
        apartment_bonus = 0.9
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio_bonus = 0.8
        apartment_bonus = 0.9
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if days > 14:
        apartment_bonus = 0.9

total_price_studio = days*studio*studio_bonus
total_price_apartment = days*apartment*apartment_bonus

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
