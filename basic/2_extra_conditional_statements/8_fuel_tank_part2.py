fuel_type = input()
fuel_liters = float(input())
bonus_card = input()

gasoline_price = 2.22
disel_price = 2.33
gas_price = 0.93

gasoline_bonus_card = 0.18
disel_bonus_card = 0.12
gas_bonus_card = 0.08

fuel_price = 0

if fuel_type == "Gas":
    if bonus_card == "Yes":
        if 20 <= fuel_liters <= 25:
            fuel_price = fuel_liters*(gas_price-gas_bonus_card)*0.92
        elif fuel_liters > 25:
            fuel_price = fuel_liters * (gas_price-gas_bonus_card) * 0.90
        else:
            fuel_price = fuel_liters * (gas_price - gas_bonus_card)
    elif bonus_card == "No":
        if 20 <= fuel_liters <= 25:
            fuel_price = (fuel_liters*gas_price)*0.92
        elif fuel_liters > 25:
            fuel_price = (fuel_liters * gas_price) * 0.90
        else:
            fuel_price = fuel_liters * gas_price


if fuel_type == "Gasoline":
    if bonus_card == "Yes":
        if 20 <= fuel_liters <= 25:
            fuel_price = fuel_liters*(gasoline_price-gasoline_bonus_card)*0.92
        elif fuel_liters > 25:
            fuel_price = fuel_liters * (gasoline_price-gasoline_bonus_card) * 0.90
        else:
            fuel_price = fuel_liters * (gasoline_price - gasoline_bonus_card)
    elif bonus_card == "No":
        if 20 <= fuel_liters <= 25:
            fuel_price = (fuel_liters*gasoline_price)*0.92
        elif fuel_liters > 25:
            fuel_price = (fuel_liters * gasoline_price) * 0.90
        else:
            fuel_price = fuel_liters * gasoline_price


if fuel_type == "Diesel":
    if bonus_card == "Yes":
        if 20 <= fuel_liters <= 25:
            fuel_price = fuel_liters*(disel_price-disel_bonus_card)*0.92
        elif fuel_liters > 25:
            fuel_price = fuel_liters * (disel_price-disel_bonus_card) * 0.90
        else:
            fuel_price = fuel_liters * (disel_price - disel_bonus_card)
    elif bonus_card == "No":
        if 20 <= fuel_liters <= 25:
            fuel_price = (fuel_liters * disel_price)*0.92
        elif fuel_liters > 25:
            fuel_price = (fuel_liters * disel_price) * 0.90
        else:
            fuel_price = fuel_liters * disel_price

print(f"{fuel_price:.2f} lv.")
