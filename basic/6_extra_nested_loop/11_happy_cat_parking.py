days = int(input())
hours = int(input())
days_counter = 0
price = 0
day_tax = 0
total_tax = 0

for d in range(1, days+1):
    days_counter += 1
    day_tax = 0
    for h in range(1, hours+1):
        if (d % 2 == 0) and (h % 2 == 1):
            price = 2.50
        elif (d % 2 == 1) and (h % 2 == 0):
            price = 1.25
        else:
            price = 1
        day_tax += price
    total_tax += day_tax
    print(f"Day: {days_counter} - {day_tax:.2f} leva")

print(f"Total: {total_tax:.2f} leva")
