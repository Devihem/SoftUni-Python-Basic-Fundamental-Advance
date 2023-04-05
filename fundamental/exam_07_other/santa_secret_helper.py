import re

key_value = int(input())
pattern_kids = r"@([a-zA-Z]+).*[^\@\-\!\:\>].*\!([G])!"

while True:
    coded_msg = input()

    if coded_msg == "end":
        break

    current_msg = ""
    for symbol in coded_msg:
        current_msg += chr(ord(symbol)- key_value)
    match = re.findall(pattern_kids, current_msg)
    if match:
        print(match[0][0])