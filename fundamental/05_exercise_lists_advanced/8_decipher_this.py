def letter_swap_5_8(word: str):
    word_in_list = list(word)
    word_in_list[1], word_in_list[-1] = word_in_list[-1], word_in_list[1]
    return "".join(word_in_list)


def numbers_to_letter_5_8(word: str):
    word_in_list = list(word)
    digit_list = []
    letter_list = []
    for symbol in word_in_list:
        if symbol.isdigit():
            digit_list.append(symbol)
        else:
            letter_list.append(symbol)
    digit_list = [chr(int("".join(digit_list)))]
    result = digit_list + letter_list
    return "".join(result)


codded_msg = input().split()
decipher_msg = [numbers_to_letter_5_8(word) for word in codded_msg]
decipher_msg = [letter_swap_5_8(word) for word in decipher_msg]
print(*decipher_msg)
