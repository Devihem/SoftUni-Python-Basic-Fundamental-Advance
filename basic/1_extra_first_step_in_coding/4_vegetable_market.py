price_vegi = float(input())
price_fruits = float(input())
weight_vegi = int(input())
weight_fruits = int(input())

vegi_income = price_vegi*weight_vegi
fruits_income = price_fruits*weight_fruits

total_income = (vegi_income+fruits_income)/1.94
print(f"{total_income:.2f}")
