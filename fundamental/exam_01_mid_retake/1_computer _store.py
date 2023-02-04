total_price = 0
taxes = 0
discount = 1
while True:
    command = input()
    if command == "regular":
        break
    elif command == "special":
        discount = 0.9
        break

    value = float(command)
    if value < 0:
        print("Invalid price!")
        continue
    total_price += value

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.2
    total_sum = (total_price + taxes) * discount
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f" Total price: {total_sum:.2f}$")
