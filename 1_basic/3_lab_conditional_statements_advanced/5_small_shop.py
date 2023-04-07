item_selected = input()
city_selected = input()
quantity = float(input())

coffee = 0
water = 0
beer = 0
sweets = 0
peanuts = 0
price = 0

if city_selected == "Varna":
    coffee = 0.45
    water = 0.70
    beer = 1.10
    sweets = 1.35
    peanuts = 1.55
elif city_selected == "Plovdiv":
    coffee = 0.40
    water = 0.70
    beer = 1.15
    sweets = 1.30
    peanuts = 1.50
elif city_selected == "Sofia":
    coffee = 0.50
    water = 0.80
    beer = 1.20
    sweets = 1.45
    peanuts = 1.60

if item_selected == "coffee":
    price = coffee * quantity
elif item_selected == "water":
    price = water * quantity
elif item_selected == "beer":
    price = beer * quantity
elif item_selected == "sweets":
    price = sweets * quantity
elif item_selected == "peanuts":
    price = peanuts * quantity

print(price)
