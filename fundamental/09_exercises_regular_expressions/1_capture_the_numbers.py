import re

regex = r"\d+"
text = input()

while text:
    matches = re.findall(regex, text)
    if matches:
        print(" ".join(matches), end=" ")
    text = input()
