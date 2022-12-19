budget = float(input())
destination = input()
season = input()
days = int(input())
bonus = 1
price = 0

if season == "Winter":
    if destination == "Dubai":
        price = 45000
        bonus = 0.7
    elif destination == "Sofia":
        price = 17000
        bonus = 1.25
    elif destination == "London":
        price = 24000

elif season == "Summer":
    if destination == "Dubai":
        price = 40000
        bonus = 0.7
    elif destination == "Sofia":
        price = 12500
        bonus = 1.25
    elif destination == "London":
        price = 20250

total_sum = days * price * bonus
diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
elif budget < total_sum:
    print(f"The director needs {diff:.2f} leva more!")
