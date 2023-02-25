input_string = input()
final_string = input_string[0]

for letter in list(input_string):
    if final_string[-1] == letter:
        continue
    final_string += letter

print(final_string)
