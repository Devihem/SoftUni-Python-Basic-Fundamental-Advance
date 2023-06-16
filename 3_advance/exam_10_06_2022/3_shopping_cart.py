def shopping_cart(*args):
    food_dict = {
        'Soup': [3],
        'Pizza': [4],
        'Dessert': [2]
    }

    for info_products in args:
        if info_products == 'Stop':
            break

        key, value = info_products
        if food_dict[key][0] > len(food_dict[key]) - 1:
            if value not in food_dict[key]:
                food_dict[key].append(value)

    for key, value in food_dict.items():
        food_dict[key] = food_dict[key][1:]

    for value in food_dict.values():
        if value:
            break
    else:
        return "No products in the cart!"

    sorted_products = sorted(food_dict.items(), key=lambda k: (-len(k[1]), k[0]))
    final_sorted_print = ''
    for meal, products in sorted_products:
        final_sorted_print += meal + ":\n"
        for product in sorted(products):
            final_sorted_print += " - "+product+"\n"
    return final_sorted_print


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
