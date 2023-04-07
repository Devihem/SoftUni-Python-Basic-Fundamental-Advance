charity_money = int(input())

collected_money = 0
counter_payment = 0
cash_counter = 0
cash_total = 0
credit_counter = 0
credit_total = 0


while collected_money < charity_money:
    command_loop = input()
    counter_payment += 1
    if command_loop == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        command_loop = int(command_loop)

    if counter_payment % 2 == 1 and command_loop <= 100:
        print("Product sold!")
        cash_counter += 1
        cash_total += command_loop
        collected_money = cash_total + credit_total
    elif counter_payment % 2 == 0 and command_loop > 10:
        print("Product sold!")
        credit_counter += 1
        credit_total += command_loop
        collected_money = cash_total + credit_total
    else:
        print("Error in transaction!")
else:
    print(f"Average CS: {cash_total / cash_counter:.2f}")
    print(f"Average CC: {credit_total / credit_counter:.2f}")
