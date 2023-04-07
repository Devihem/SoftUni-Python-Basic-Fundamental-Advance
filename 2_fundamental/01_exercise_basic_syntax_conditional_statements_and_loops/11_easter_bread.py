budget = float(input())

flour_kg_price = float(input())
eggs_pack_price = flour_kg_price * 0.75
milk_price_l = flour_kg_price * 1.25
bread_made = 0
colored_eggs = 0
current_milk_l = 0
total_price_for_1 = milk_price_l + eggs_pack_price + flour_kg_price

while True:

    if current_milk_l < 0.25 and budget < total_price_for_1:
        break
    elif budget < (eggs_pack_price + flour_kg_price):
        break
    elif current_milk_l < 0.25:
        current_milk_l = 1
        budget -= milk_price_l

    budget -= (eggs_pack_price + flour_kg_price)
    current_milk_l -= 0.25
    bread_made += 1
    colored_eggs += 3

    if bread_made % 3 == 0:
        colored_eggs = colored_eggs - (bread_made - 2)

print(f"You made {bread_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
