items_list = input().split("|")
budget = float(input())
bought_item_list = []
total_price = 0
profit = 0
total_money_from_sell = 0

for item in items_list:
    item = item.split("->")
    if item[0] == "Clothes" and 0 <= float(item[1]) <= 50:
        pass
    elif item[0] == "Shoes" and 0 <= float(item[1]) <= 35:
        pass
    elif item[0] == "Accessories" and 0 <= float(item[1]) <= 20.50:
        pass
    else:
        continue
    current_price = float(item[1])
    if budget >= current_price:
        budget -= current_price
        total_price += current_price
        bought_item_list.append(round(current_price * 1.40, 2))

for item in bought_item_list:
    total_money_from_sell += float(item)

formatted_bought_item_list = ["%.2f" % item for item in bought_item_list]


profit = total_money_from_sell - total_price
print(*formatted_bought_item_list)
print(f"Profit: {profit:.2f}")
if (budget + total_money_from_sell) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
