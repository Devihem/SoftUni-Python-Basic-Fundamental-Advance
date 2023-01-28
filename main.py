word = "122sadasd"
word_in_list = list(word)
digit_list = []
letter_list = []
for symbol in word_in_list:
    if symbol.isdigit():
        digit_list.append(symbol)
    else:
        letter_list.append(symbol)
digit_list = [chr(int("".join(digit_list)))]
final_list = digit_list + letter_list
print(digit_list)
print(letter_list)
print(final_list)