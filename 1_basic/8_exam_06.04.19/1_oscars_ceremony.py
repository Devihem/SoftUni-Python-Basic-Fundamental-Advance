rent_price = int(input())

trophy = rent_price * 0.7
food = trophy * 0.85
sound = food / 2
total_sum = rent_price + trophy + food + sound

print(f"{total_sum:.2f}")
