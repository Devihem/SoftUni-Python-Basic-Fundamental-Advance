days_loop = int(input())
hours = int(input())
price_h = 0
day_price = 0
total_sum = 0

for d in range(1, days_loop+1):
    for h in range(1, hours+1):
        if d % 2 == 0 and h % 2 != 0:
            price = 2.5
        elif d % 2 != 0 and h % 2 == 0:
            price = 1.25
        else:
            price = 1
        day_price += price

    print(f"Day: {d} - {day_price:.2f} leva")
    total_sum += day_price
    day_price = 0

print(f"Total: {total_sum:.2f} leva")
