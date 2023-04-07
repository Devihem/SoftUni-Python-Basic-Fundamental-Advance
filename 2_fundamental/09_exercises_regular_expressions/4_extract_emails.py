import re

text_input = input()
pattern = r"(^|(?<= ))[a-zA-Z0-9]+([-._][a-zA-Z0-9]+)*[@]([a-zA-Z]+[-.])*[a-zA-Z]+[.][a-zA-Z]+[a-zA-Z]+"
matches = re.finditer(pattern, text_input)
for match in matches:
    print(match.group())
