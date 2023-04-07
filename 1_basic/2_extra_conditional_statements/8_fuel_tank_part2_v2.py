fuel_type = input()
fuel_liters = float(input())
bonus_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_price = 0

if bonus_card == "Yes":
    gasoline_price = 2.22-0.18
    diesel_price = 2.33-0.12
    gas_price = 0.93-0.08

if fuel_type == "Gas":
    total_price = gas_price * fuel_liters
elif fuel_type == "Gasoline":
    total_price = gasoline_price * fuel_liters
elif fuel_type == "Diesel":
    total_price = diesel_price * fuel_liters

if fuel_liters > 25:
    total_price_end = total_price*0.9
elif 20 <= fuel_liters < 25:
    total_price_end = total_price*0.92
else:
    total_price_end = total_price

print(f"{total_price_end:.2f} lv.")
