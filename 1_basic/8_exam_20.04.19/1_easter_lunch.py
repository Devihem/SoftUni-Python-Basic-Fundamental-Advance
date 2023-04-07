easter_bread_number = int(input())
eggs_packs_number = int(input())
cookiges_kg = int(input())

easter_bread_price = 3.2
eggs_pack_price = 4.35
cookies_kg_price = 5.40
eggs_dye = 12 * 0.15

total_sum = easter_bread_price * easter_bread_number + cookies_kg_price * cookiges_kg + (eggs_pack_price + eggs_dye) * eggs_packs_number


print(f"{total_sum:.2f}")
