budget = float(input())
number_tv_shows_loop = int(input())
total_sum = 0

for i in range(0, number_tv_shows_loop):
    tv_show_name = input()
    price = float(input())

    if tv_show_name == "Thrones":
        price *= 0.5
    elif tv_show_name == "Lucifer":
        price *= 0.6
    elif tv_show_name == "Protector":
        price *= 0.7
    elif tv_show_name == "TotalDrama":
        price *= 0.8
    elif tv_show_name == "Area":
        price *= 0.9

    total_sum += price

if budget >= total_sum:
    print(f"You bought all the series and left with {budget - total_sum:.2f} lv.")
else:
    print(f"You need {total_sum - budget:.2f} lv. more to buy the series!")
