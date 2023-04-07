random_string = input()
all_digits = ""
all_letters = ""
all_other = ""

for char in list(random_string):
    if char.isdigit():
        all_digits += char
    elif char.isalpha():
        all_letters += char
    else:
        all_other += char

print(all_digits)
print(all_letters)
print(all_other)
