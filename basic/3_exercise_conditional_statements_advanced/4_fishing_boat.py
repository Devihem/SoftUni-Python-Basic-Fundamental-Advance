group_budget = int(input())
season = input()
fishermen = int(input())

ship_price = 0
bonus = 0

if season == "Spring":
    ship_price = 3000
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
elif season == "Winter":
    ship_price = 2600

if fishermen <= 6:
    bonus = 0.9
elif 7 <= fishermen <= 11:
    bonus = 0.85
elif fishermen >= 12:
    bonus = 0.75

total_sum = ship_price * bonus

if season != "Autumn" and fishermen % 2 == 0:
    total_sum_extra = total_sum*0.95
else:
    total_sum_extra = total_sum

diff = abs(group_budget-total_sum_extra)

if group_budget >= total_sum_extra:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
