strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
malini_kg = float(input())
strawberry_kg = float(input())

malini_price = strawberry_price * 0.5
oranges_price = malini_price * 0.6
bananas_price = malini_price * 0.2

total_sum = bananas_price * bananas_kg + malini_price * malini_kg + oranges_price * oranges_kg + strawberry_kg * strawberry_price

print(f"{total_sum:.2f}")

