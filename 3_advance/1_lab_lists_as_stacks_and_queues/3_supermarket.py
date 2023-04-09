customer_list = []
paid_index = 0
while True:
    customer_or_command = input()
    if customer_or_command == "End":
        break
    elif customer_or_command == "Paid":
        paid_index = len(customer_list)
    else:
        customer_list.append(customer_or_command)
count = len(customer_list[paid_index:])

[print(f"{customer}") for customer in customer_list[:paid_index]]
print(f"{count} people remaining.")
