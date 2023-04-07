phase = input()
ticket_type = input()
total_tickets = int(input())
photo = input()
t_price = 0
price = 0
extra_price = 0

if phase == "Quarter final":
    if ticket_type == "Standard":
        price = 55.5
    elif ticket_type == "Premium":
        price = 105.2
    elif ticket_type == "VIP":
        price = 118.9

if phase == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40

if phase == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400

if photo == "Y":
    extra_price = 40

if price * total_tickets > 4000:
    extra_price = 0
    price = price * 0.75
elif price * total_tickets > 2500:
    price = price * 0.9

t_price = (price + extra_price) * total_tickets

print(f"{t_price:.2f}")
