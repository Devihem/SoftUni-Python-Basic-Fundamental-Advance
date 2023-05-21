def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == 'odd':
            kwargs[key] = [x for x in value if x % 2 == 1]
        elif key == 'even':
            kwargs[key] = [x for x in value if x % 2 == 0]
    sorted_list = sorted(kwargs.items(), key=lambda k: -len(k[1]))
    return {data[0]: data[1] for data in sorted_list}


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
