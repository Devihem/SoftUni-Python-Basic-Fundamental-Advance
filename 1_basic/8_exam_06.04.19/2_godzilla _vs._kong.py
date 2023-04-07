budget = float(input())
statists = int(input())
price_costume_statist = float(input())

decore = budget * 0.10
costumes = statists * price_costume_statist
if statists > 150:
    costumes = costumes * 0.90

total_sum = costumes + decore
diff = abs(total_sum - budget)

if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
elif total_sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")