def read_next(*args):
    all_items_list = []
    for item in args:
        for symb in item:
            all_items_list.append(str(symb))

    while all_items_list:
        yield all_items_list.pop(0)


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
