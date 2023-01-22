def making_ord_to_char_list_4_3(starting_symbol,final_symbol):
    list_ascii_numbers = []
    for ascii_ord in range(ord(starting_symbol_excluded) + 1, ord(final_symbol_excluded)):
        list_ascii_numbers.append(chr(ascii_ord))
    return list_ascii_numbers


starting_symbol_excluded = input()
final_symbol_excluded = input()

new_reformated_list = making_ord_to_char_list_4_3(starting_symbol_excluded, final_symbol_excluded)
print(*new_reformated_list)
