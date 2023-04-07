import re

regex = "(\\+359 [2] [\\d]{3} [\\d]{4}|\\+359-[2]-[\\d]{3}-[\\d]{4})\\b"
phone_numbers = input()
matches = re.findall(regex, phone_numbers)
print(", ".join(matches))
