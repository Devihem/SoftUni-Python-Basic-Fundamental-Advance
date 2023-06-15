def shopping_list(budget, **kwargs):
    budget = budget
    counter = 0
    print_list = []
    if budget >= 100:
        for product, info in kwargs.items():
            price, quantity = info
            total_price = price * quantity
            if total_price <= budget:
                budget -= total_price
                print_list.append(f"You bought {product} for {total_price:.2f} leva.")
                counter += 1
                if counter == 5:
                    return '\n'.join(print_list)
        else:
            return '\n'.join(print_list)

    return "You do not have enough budget."


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

#
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
#
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))