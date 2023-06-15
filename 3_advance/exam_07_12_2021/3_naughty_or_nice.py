def naughty_or_nice_list(kids_list, *args, **kwargs):

    nice_list = []
    naughty_list = []
    not_found_list = []

    #  Handle the ARGS list
    for command in args:
        index, state = command.split('-')
        index_counter = 0

        for kids_index, kids_name in kids_list:
            if kids_index == int(index):
                index_counter += 1

        if index_counter == 1:
            for index_tuple in range(len(kids_list)):
                if kids_list[index_tuple][0] == int(index):
                    if state == 'Nice':
                        nice_list.append(kids_list.pop(index_tuple)[1])
                    else:
                        naughty_list.append(kids_list.pop(index_tuple)[1])
                    break

    # handle KWARGS list
    for key_name, key_state in kwargs.items():

        key_count_in_list_kids = 0
        for kids_index, kids_name in kids_list:
            if kids_name == key_name:
                key_count_in_list_kids += 1

        if key_count_in_list_kids == 1:
            for index_tuple in range(len(kids_list)):
                if kids_list[index_tuple][1] == key_name:
                    if key_state == 'Nice':
                        nice_list.append(kids_list.pop(index_tuple)[1])
                    else:
                        naughty_list.append(kids_list.pop(index_tuple)[1])
                    break

    for index_tuple in range(len(kids_list)):
        not_found_list.append(kids_list[index_tuple][1])
    kids_list.clear()
    final_string = ''
    if nice_list:
        final_string += f'Nice: {", ".join(nice_list)}\n'
    if naughty_list:
        final_string += f'Naughty: {", ".join(naughty_list)}\n'
    if not_found_list:
        final_string += f'Not found: {", ".join(not_found_list)}'
    return final_string




print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
