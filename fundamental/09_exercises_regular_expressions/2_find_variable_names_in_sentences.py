import re

pattern = r"\b[_]{1}(?P<word>[a-zA-Z]+)\b"
text = input()
matches = re.findall(pattern, text)
print(*matches, sep=",")
