def shop_from_grocery_list(*shopping_info):
    budget = shopping_info[0]
    needed_to_bought_set = set(shopping_info[1])
    price_products = shopping_info[2:]
    items_already_bought = set()

    for item, value in price_products:
        if item in needed_to_bought_set and item not in items_already_bought:
            if value <= budget:
                items_already_bought.add(item)
                budget -= value
            else:
                break

    if len(needed_to_bought_set) == len(items_already_bought):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(needed_to_bought_set.difference(items_already_bought))}."


print(shop_from_grocery_list(
    100,
    ['zola','mola','fola','foas', 'koad', 'meat'],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))