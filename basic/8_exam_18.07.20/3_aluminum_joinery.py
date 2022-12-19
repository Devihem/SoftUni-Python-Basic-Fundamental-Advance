units = int(input())
joints_size = input()
delivery = input()
price = 0
discount = 0



if joints_size == "90X130":
    price = 110
    if 30 < units <= 60:
        discount = 5
    elif units > 60:
        discount = 8
elif joints_size == "100X150":
    price = 140
    if 40 < units <= 80:
        discount = 6
    elif units > 80:
        discount = 10
elif joints_size == "130X180":
    price = 190
    if 20 < units <= 50:
        discount = 7
    elif units > 50:
        discount = 12
elif joints_size == "200X300":
    price = 250
    if 25 < units <= 50:
        discount = 9
    elif units > 60:
        discount = 14

total_sum = units * price * (1 - discount/100)

if delivery == "With delivery":
    total_sum += 60

if units > 99:
    total_sum = total_sum * 0.96

if units < 10:
    print("Invalid order")
else:
    print(f"{total_sum:.2f} BGN")
