type_of_drink = input()
sugar_option = input()
drinks_count = int(input())
no_sugar_bonus = 1
over_4_bonus = 1
drink_price = 0

if type_of_drink == "Espresso":
    if drinks_count > 4:
        over_4_bonus = 0.75
    if sugar_option == "Without":
        drink_price = 0.9
        no_sugar_bonus = 0.65
    elif sugar_option == "Normal":
        drink_price = 1
    elif sugar_option == "Extra":
        drink_price = 1.2

elif type_of_drink == "Cappuccino":
    if sugar_option == "Without":
        drink_price = 1
        no_sugar_bonus = 0.65
    elif sugar_option == "Normal":
        drink_price = 1.2
    elif sugar_option == "Extra":
        drink_price = 1.6

elif type_of_drink == "Tea":
    if sugar_option == "Without":
        drink_price = 0.5
        no_sugar_bonus = 0.65
    elif sugar_option == "Normal":
        drink_price = 0.6
    elif sugar_option == "Extra":
        drink_price = 0.7

total_sum = drink_price * no_sugar_bonus * drinks_count * over_4_bonus

if total_sum > 15:
    total_sum *= 0.80

print(f"You bought {drinks_count} cups of {type_of_drink} for {total_sum:.2f} lv.")
