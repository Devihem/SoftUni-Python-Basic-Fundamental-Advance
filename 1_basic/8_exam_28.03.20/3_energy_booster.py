type_fruit = input()
size = input()
units = int(input())
price = 0
bonus = 1

if size == "small":
    size = 2
    if type_fruit == "Watermelon":
        price = 56
    elif type_fruit == "Mango":
        price = 36.66
    elif type_fruit == "Pineapple":
        price = 42.10
    elif type_fruit == "Raspberry":
        price = 20

elif size == "big":
    size = 5
    if type_fruit == "Watermelon":
        price = 28.70
    elif type_fruit == "Mango":
        price = 19.60
    elif type_fruit == "Pineapple":
        price = 24.80
    elif type_fruit == "Raspberry":
        price = 15.20

total_sum = units * size * price
if 400 <= total_sum <= 1000:
    bonus = 0.85
elif total_sum > 1000:
    bonus = 0.5

total_sum_with_bonus = total_sum * bonus

print(f"{total_sum_with_bonus:.2f} lv.")
