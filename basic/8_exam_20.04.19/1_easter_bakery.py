flour_price = float(input())
flour_needed = float(input())
sugar_needed = float(input())
eggs_packs_needed = int(input())
yeast_packs_needed = int(input())

sugar_price = flour_price * 0.75
eggs_pack_price = flour_price * 1.1
yeast_pack_price = sugar_price * 0.2

total_sum = flour_needed * flour_price + sugar_needed * sugar_price + eggs_packs_needed * eggs_pack_price \
            + yeast_packs_needed * yeast_pack_price

print(f"{total_sum:.2f}")
