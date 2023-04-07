budget = float(input())
payment = 0
while budget >= 0:
    cast_name = input()

    if cast_name == "ACTION":
        break
    elif len(cast_name) > 15:
        payment = budget * 0.2
    else:
        payment = float(input())

    budget = budget - payment

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
elif budget < 0:
    print(f"We need {-budget:.2f} leva for our actors.")

