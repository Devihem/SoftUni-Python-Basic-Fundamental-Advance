def grocery_store(**kwargs):

    result = sorted(kwargs.items(), key=lambda k: (-k[1], -len(k[0]), k[0]))
    final_list_result = [f'{key}: {value}' for key, value in result]
    return '\n'.join(final_list_result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

print(grocery_store(
    bread=5,
    zpasta=12,
    aaaggs=12,
))
