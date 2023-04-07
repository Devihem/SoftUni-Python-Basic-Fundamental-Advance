season = input()
km = float(input())
price_per_km = 0

if km <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.90
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < km <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    elif season == "Winter":
        price_per_km = 1.25
elif 10000 < km <= 20000:
    price_per_km = 1.45

total = price_per_km * km * 4
with_tax_total = total * 0.9

print(f"{with_tax_total:.2f}")
