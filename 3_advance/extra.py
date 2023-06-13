def shop_from_grocery_list(budget, grocery_list, *products):
    grocery_list_dict = {item: False for item in grocery_list if grocery_list}

    if grocery_list_dict:
        for product in products:
            if product[0] in grocery_list:
                if not grocery_list_dict[product[0]]:
                    if budget >= product[1]:
                        grocery_list_dict[product[0]] = True
                        budget -= product[1]
                    else:
                        break

    if all(value for value in grocery_list_dict.values()):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: " \
               f"{', '.join([item for item, value in grocery_list_dict.items() if value == False])}."

print(shop_from_grocery_list(
    100,
    [],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))