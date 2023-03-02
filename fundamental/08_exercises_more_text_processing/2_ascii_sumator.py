starting_symbol_ord = ord(input())
final_symbol_ord = ord(input())
string = input()
final_sum_result = 0

for char in string:
    if starting_symbol_ord < ord(char) < final_symbol_ord:
        final_sum_result += ord(char)
print(final_sum_result)
