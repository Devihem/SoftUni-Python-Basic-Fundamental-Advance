movie = input()
option = input()
tickets = int(input())

price = 0
bonus = 1

if movie == "John Wick":
    if option == "Drink":
        price = 12
    elif option == "Popcorn":
        price = 15
    elif option == "Menu":
        price = 19

elif movie == "Star Wars":
    if option == "Drink":
        price = 18
    elif option == "Popcorn":
        price = 25
    elif option == "Menu":
        price = 30
    if tickets > 3:
        bonus = 0.7

elif movie == "Jumanji":
    if option == "Drink":
        price = 9
    elif option == "Popcorn":
        price = 11
    elif option == "Menu":
        price = 14
    if tickets == 2:
        bonus = 0.85

total_sum = tickets * price * bonus

print(f"Your bill is {total_sum:.2f} leva.")
