eggs_in_store = int(input())
operator = 1
total_eggs_bought = 0

while True:
    command = input()
    if command == "Close":
        print(f"Store is closed!")
        print(f"{total_eggs_bought} eggs sold.")
        break
    elif command == "Buy":
        eggs_buy = int(input())
        if eggs_in_store - eggs_buy < 0:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_store}.")
            break
        eggs_in_store = eggs_in_store - eggs_buy
        total_eggs_bought += eggs_buy

    elif command == "Fill":
        eggs_fill = int(input())
        eggs_in_store += eggs_fill
