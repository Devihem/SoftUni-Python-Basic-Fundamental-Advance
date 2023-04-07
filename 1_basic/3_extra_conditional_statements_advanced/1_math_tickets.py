budget = float(input())
ticket_type = input()
group_size = int(input())

ticket_price = 0
transport_tax = 0

if ticket_type == "VIP":
    ticket_price = 499.99 * group_size
elif ticket_type == "Normal":
    ticket_price = 249.99 * group_size

if 1 <= group_size <= 4:
    transport_tax = budget * 0.75
elif 5 <= group_size <= 9:
    transport_tax = budget * 0.60
elif 10 <= group_size <= 24:
    transport_tax = budget * 0.50
elif 25 <= group_size <= 49:
    transport_tax = budget * 0.40
elif group_size >= 50:
    transport_tax = budget * 0.25

total_sum = ticket_price + transport_tax
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Yes! You have {diff:.2f} leva left.")
elif total_sum > budget:
    print(f"Not enough money! You need {diff:.2f} leva.")
