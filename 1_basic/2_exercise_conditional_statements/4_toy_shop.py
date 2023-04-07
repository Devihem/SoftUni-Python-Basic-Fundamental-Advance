puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

vacation = float(input())
puzzle_order = int(input())
doll_order = int(input())
bear_order = int(input())
minion_order = int(input())
truck_order = int(input())

total_units = puzzle_order+doll_order+bear_order+minion_order+truck_order

if total_units >= 50:
    total_sum = (puzzle_order * puzzle + doll_order * doll + bear_order * bear +
                 minion_order * minion + truck_order * truck)*0.75
else:
    total_sum = puzzle_order * puzzle + doll_order * doll + bear_order * bear +\
                minion_order * minion + truck_order * truck

rent_total_sum = total_sum*0.9

diff=abs(rent_total_sum-vacation)

if rent_total_sum >= vacation:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")


