town = input()
total = float(input())
bonus = "error"

if town == "Sofia":
    if 0 <= total <= 500:
        bonus = total * 0.05
    elif 500 < total <= 1000:
        bonus = total * 0.07
    elif 1000 < total <= 10000:
        bonus = total * 0.08
    elif total > 10000:
        bonus = total * 0.12
elif town == "Varna":
    if 0 <= total <= 500:
        bonus = total*0.045
    elif 500 < total <= 1000:
        bonus = total * 0.075
    elif 1000 < total <= 10000:
        bonus = total * 0.10
    elif total > 10000:
        bonus = total * 0.13
elif town == "Plovdiv":
    if 0 <= total <= 500:
        bonus = total*0.055
    elif 500 < total <= 1000:
        bonus = total * 0.08
    elif 1000 < total <= 10000:
        bonus = total * 0.12
    elif total > 10000:
        bonus = total * 0.145

if bonus != "error":
    print(f"{bonus:.2f}")
else:
    print(bonus)
