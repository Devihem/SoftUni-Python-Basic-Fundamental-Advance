def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda k: (-len(k[1]), (k[0])))
    result = []
    for item, quantity in kwargs:
        result.append(item)
        result.extend(sorted(quantity, reverse=True))
    return '\n'.join(str(x) for x in result)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
