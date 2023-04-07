import re

pattern = "(^|(?<=\\s))-?(0|[1-9][\\d]*)(\\.\\d+)?($|(?=\\s))"
numbers = input()
matches = re.finditer(pattern, numbers)
for match in matches:
    print(match.group(), end=" ")
