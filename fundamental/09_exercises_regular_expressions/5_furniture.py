import re

pattern = r"(?i)>>([a-z]+)<<(\d+[.]?\d+)!(\d+)"
total_sum = 0
bought_items_list = []

while True:

    command = input()
    if command == "Purchase":
        break
    match = re.findall(pattern, command)
    if match:
        total_sum += float(match[0][1]) * float(match[0][2])
        bought_items_list.append(match[0][0])

print("Bought furniture:")
[print(item) for item in bought_items_list]
print(f"Total money spend: {total_sum:.2f}")
