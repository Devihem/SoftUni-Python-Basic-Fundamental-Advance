from math import ceil

budget = float(input())
students = int(input())
flour = float(input())
one_egg = float(input())
one_apron = float(input())
bonus_free_flour = students // 5
flour_price = flour * (students - bonus_free_flour)
eggs_price = one_egg * students * 10
aprons_price = ceil(students * 1.2) * one_apron
total_price = flour_price + eggs_price + aprons_price

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$")
else:
    print(f"{total_price-budget:.2f}$ more needed.")
