import re

pattern = r"\%([A-Z][a-z]*)\%[^\%\$\.\|]*\<(\w+)\>[^\%\$\.\|]*\|(\d+)\|[^\%\$\.\|\d]*(\d+[\.]?[\d+]*)\$$"
total_income = 0

while True:
    command = input()
    if command == "end of shift":
        print(f"Total income: {total_income:.2f}")
        break
    match = re.findall(pattern, command)
    if match:
        # regex transfer to variables
        name, product, quantity, price = match[0][0], match[0][1], match[0][2], match[0][3]
        current_sum = int(quantity) * float(price)
        total_income += current_sum
        print(f"{name}: {product} - {current_sum:.2f}")
