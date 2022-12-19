from math import ceil, floor

days = int(input())
food_total = int(input())
dog_eat = float(input())
cat_eat = float(input())
turtle_eat = float(input())

needed_food = (dog_eat+cat_eat+(turtle_eat/1000))*days

remaining_food = abs(food_total-needed_food)

if needed_food <= food_total:
    print(f"{floor(remaining_food)} kilos of food left.")
elif needed_food > food_total:
    print(f"{ceil(remaining_food)} more kilos of food are needed.")
