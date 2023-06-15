def words_sorting(*words):
    words_dict = {}
    total_sum = 0
    for word in words:
        word_sum = 0
        for char in word:
            word_sum += ord(char)
            total_sum += ord(char)
        words_dict[word] = word_sum

    if total_sum % 2 == 0:
        new_sorted = sorted(words_dict.items())
    else:
        new_sorted = sorted(words_dict.items(), key=lambda k: -k[1])

    print_str = ''
    for key_str, value_str in new_sorted:
        print_str += f'{key_str} - {value_str}\n'
    return print_str

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
