from math import floor
from math import  ceil

days_off = int(input())
food_kg = int(input())
deer1_food = float(input())
deer2_food = float(input())
deer3_food = float(input())

total_food_p_day = deer3_food + deer2_food + deer1_food
total_food_max = total_food_p_day * days_off

diff = abs(total_food_max - food_kg)

if total_food_max <= food_kg:
    print(f"{floor(diff)} kilos of food left.")
elif total_food_max > food_kg:
    print(f"{ceil(diff)} more kilos of food are needed.")
