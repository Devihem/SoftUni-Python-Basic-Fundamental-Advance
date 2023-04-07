people = int(input())
season = input()

bonus = 1
price = 1

if people <= 5:
    if season == "spring":
        price = 50
    elif season == "summer":
        bonus = 0.85
        price = 48.50
    elif season == "autumn":
        price = 60
    elif season == "winter":
        bonus = 1.08
        price = 86

elif people > 5:
    if season == "spring":
        price = 48
    elif season == "summer":
        bonus = 0.85
        price = 45
    elif season == "autumn":
        price = 49.50
    elif season == "winter":
        bonus = 1.08
        price = 85

total_sum = price * bonus * people

print(f"{total_sum:.2f} leva.")