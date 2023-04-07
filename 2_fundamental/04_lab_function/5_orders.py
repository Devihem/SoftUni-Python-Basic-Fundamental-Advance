product = input()
quantity = int(input())


def price_list_4_5(d_product, d_quantity):
    price = 0
    if d_product == "coffee":
        price = 1.50
    elif d_product == "coke":
        price = 1.40
    elif d_product == "water":
        price = 1.00
    elif d_product == "snacks":
        price = 2.00
    return price * d_quantity


print(f"{price_list_4_5(product, quantity):.2f}")
