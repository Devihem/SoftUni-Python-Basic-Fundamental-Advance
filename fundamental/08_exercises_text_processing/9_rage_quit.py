rage_string = input()
current_string = ""
final_string = ""
unique_symbols = ""
index = -1
for item in rage_string:
    index += 1
    if item.isdigit():
        digit = item
        if index + 1 < len(rage_string):
            if rage_string[index+1].isdigit():
                digit = item+rage_string[index+1]
        final_string += current_string * int(digit)
        current_string = ""
    else:
        current_string += item.upper()

for letter_symbol in final_string:
    if letter_symbol not in unique_symbols:
        unique_symbols += letter_symbol
print(f"Unique symbols used: {len(unique_symbols)}")
print(final_string)
