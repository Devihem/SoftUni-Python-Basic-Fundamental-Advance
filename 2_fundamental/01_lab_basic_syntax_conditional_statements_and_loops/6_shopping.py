budget = int(input())

while True:
    new_item_bought = input()
    if new_item_bought == "End":
        print("You bought everything needed.")
        break
    else:
        new_item_bought = int(new_item_bought)

    if budget - new_item_bought < 0:
        print("You went in overdraft!")
        break

    budget -= new_item_bought

