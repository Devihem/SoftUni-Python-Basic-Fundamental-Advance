import re

pattern = r"\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})\b"
dates = input()
matches = re.finditer(pattern, dates)
for match in matches:
    print(f"Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}")
