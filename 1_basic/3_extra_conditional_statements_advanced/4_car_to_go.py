budget = float(input())
season = input()

car = 0
car_class = 0
price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Winter":
        car = "Jeep"
        price = budget * 0.65
    elif season == "Summer":
        car = "Cabrio"
        price = budget*0.35

elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Winter":
        car = "Jeep"
        price = budget * 0.80
    elif season == "Summer":
        car = "Cabrio"
        price = budget*0.45

elif budget > 500:
    car_class = "Luxury class"
    car = "Jeep"
    price = budget * 0.9

print(car_class)
print(f"{car} - {price:.2f}")
