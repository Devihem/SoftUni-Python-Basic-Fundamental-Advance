budget = float(input())
needed_petrol_l = float(input())
day = input()

petrol_l_price = 2.1
man_to_hire = 100
bonus = 0

if day == "Saturday":
    bonus = 10
elif day == "Sunday":
    bonus = 20

total_sum = (needed_petrol_l * petrol_l_price + man_to_hire) * (1 - bonus / 100)
diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
