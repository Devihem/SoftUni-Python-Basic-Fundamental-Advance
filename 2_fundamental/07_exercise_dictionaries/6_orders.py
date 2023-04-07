shopping_dict = {}
while True:

    order = input().split()
    if order[0] == "buy":
        break
    product = order[0]
    price = float(order[1])
    quantity = int(order[2])

    if product not in shopping_dict:
        shopping_dict[product] = price, quantity
    else:
        shopping_dict[product] = price, shopping_dict[product][1] + quantity

[print(f"{product} -> {shopping_dict[product][0] * shopping_dict[product][1]:.2f}") for product in shopping_dict]