days_hunting = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
current_plunder = 0
for day in range(1, days_hunting+1):
    current_plunder += daily_plunder

    if day % 3 == 0:
        current_plunder += daily_plunder/2

    if day % 5 == 0:
        current_plunder *= 0.7

if current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {current_plunder/expected_plunder * 100:.2f}% of the plunder.")
