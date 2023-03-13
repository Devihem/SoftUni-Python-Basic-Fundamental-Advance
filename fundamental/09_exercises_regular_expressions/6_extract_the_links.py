import re

pattern = r"www[.][a-zA-Z0-9]+(-[a-zA-Z0-9]+)*[.][A-Za-z]+(.[a-z]+)*"
website_list = []
text = input()
while text:
    match = re.search(pattern, text)
    if match:
        print(match.group())
    text = input()
