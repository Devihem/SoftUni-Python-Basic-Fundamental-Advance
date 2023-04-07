orders_loop = int(input())
total_income = 0

for orders in range(0, orders_loop):

    coffee_price = float(input())
    days = int(input())
    coffee_per_day = int(input())

    if 0.01 > coffee_price or coffee_price > 100 or 1 > days or days > 31 or 1 > \
            coffee_per_day or coffee_per_day > 2000:
        continue

    total_price = coffee_price * days * coffee_per_day
    print(f"The price for the coffee is: ${total_price:.2f}")
    total_income += total_price

print(f"Total: ${total_income:.2f}")
