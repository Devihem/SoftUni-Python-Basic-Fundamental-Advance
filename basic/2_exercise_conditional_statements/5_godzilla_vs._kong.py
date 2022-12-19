money_for_movie = float(input())
people = int(input())
costume_price = float(input())

background = money_for_movie*0.1

if people > 150:
    costume_price = costume_price*0.9

total_cost = people*costume_price+background

diff=abs(total_cost-money_for_movie)

if total_cost > money_for_movie:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
elif total_cost <= money_for_movie:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")