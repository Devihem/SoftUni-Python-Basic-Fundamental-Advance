budget = float(input())
item = input()
item_price = 0
counter = 0
total_budget = budget

while item != "Stop":
    item_price = float(input())
    counter += 1
    if counter % 3 == 0:
        item_price = item_price * 0.5

    if budget - item_price < 0:
        print("You don't have enough money!")
        print(f"You need {item_price - budget:.2f} leva!")
        break
    else:
        budget -= item_price

    item = input()

else:
    print(f"You bought {counter} products for {total_budget - budget:.2f} leva.")