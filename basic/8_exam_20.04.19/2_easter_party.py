guests = int(input())
dinner_price = float(input())
budget = float(input())

if 10 <= guests <= 15:
    dinner_price = dinner_price * 0.85
elif 15 < guests <= 20:
    dinner_price = dinner_price * 0.80
elif guests > 20:
    dinner_price = dinner_price * 0.75

cake_price = budget * 0.10

total_sum = cake_price + guests * dinner_price

diff = abs(total_sum - budget)
if total_sum <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
elif total_sum > budget:
    print(f"No party! {diff:.2f} leva needed.")
