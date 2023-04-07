from math import  ceil
guests = int(input())
budget = int(input())

easter_breads = ceil(guests / 3)
eggs = guests * 2

easter_breads_price = 4
egg_price = 0.45

total_sum = eggs * egg_price + easter_breads_price * easter_breads


if budget >= total_sum:
    print(f"Lyubo bought {easter_breads} Easter bread and {eggs} eggs.")
    print(f"He has {budget - total_sum:.2f} lv. left.")
elif budget < total_sum:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_sum - budget:.2f} lv. more.")
