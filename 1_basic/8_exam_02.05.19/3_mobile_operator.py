period = input()
option = input()
internet = input()
months = int(input())
price = 0
internet_price = 0
y2_bonus = 0
total_sum = 0

if period == "one":
    if option == "Small":
        price = 9.98
    elif option == "Middle":
        price = 18.99
    elif option == "Large":
        price = 25.98
    elif option == "ExtraLarge":
        price = 35.99

elif period == "two":
    y2_bonus = 3.75
    if option == "Small":
        price = 8.58
    elif option == "Middle":
        price = 17.09
    elif option == "Large":
        price = 23.59
    elif option == "ExtraLarge":
        price = 31.79

if internet == "yes":
    if price <= 10:
        internet_price = 5.50
    elif 10 < price <= 30:
        internet_price = 4.35
    elif price > 30:
        internet_price = 3.85

total_sum = ((price + internet_price)*(1 - y2_bonus / 100)) * months
print(f"{total_sum:.2f} lv.")
