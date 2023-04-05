import re

msg_count = int(input())

pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1\:\s[\[]([\d]+)[\]][\|][\[]([\d]+)[\]][\|][\[]([\d]+)[\]][\|]$"
for msg in range(msg_count):
    new_msg = input()
    valid_msg = re.findall(pattern, new_msg)
    if valid_msg:
        coded_string = chr(int(valid_msg[0][2])) + chr(int(valid_msg[0][3])) + chr(int(valid_msg[0][4]))
        print(f"{valid_msg[0][1]}: {coded_string}")
    else:
        print("Valid message not found!")