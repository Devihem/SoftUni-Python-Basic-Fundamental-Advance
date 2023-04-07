rent_place_price = float(input())

cake_price = 0.2 * rent_place_price
drinks_price = cake_price * 0.55
animator = rent_place_price / 3

total = cake_price + rent_place_price + drinks_price + animator

print(f"{total:.1f}")