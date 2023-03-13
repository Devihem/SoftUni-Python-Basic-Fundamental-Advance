import re
text = input()
searched_word = input()
pattern = rf"\b{searched_word}\b"

match = re.findall(pattern, text, re.I)
print(len(match))
