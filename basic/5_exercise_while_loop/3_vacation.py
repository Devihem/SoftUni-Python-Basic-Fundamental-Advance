vacation_money = float(input())
saved_money = float(input())
options = ""
spend_counter = 0
total_days = 0

while saved_money < vacation_money:

    options = input()
    money_amount = float(input())
    total_days += 1

    if options == "save":
        saved_money += money_amount
        spend_counter = 0
    elif options == "spend":
        spend_counter += 1
        saved_money -= money_amount
        if saved_money < 0:
            saved_money = 0

    if spend_counter == 5:
        print("You can't save the money.")
        print(total_days)
        break
else:
    print(f"You saved the money for {total_days} days.")
