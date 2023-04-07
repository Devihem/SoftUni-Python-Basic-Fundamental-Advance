total_budget = float(input())
night_stays = int(input())
night_stays_price = float(input())
extra_fees = int(input())

if night_stays > 7:
    night_stays_price = night_stays_price * 0.95


total_money_spend = night_stays * night_stays_price + total_budget * (extra_fees/100)
diff = abs(total_money_spend - total_budget)

if total_money_spend <= total_budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
