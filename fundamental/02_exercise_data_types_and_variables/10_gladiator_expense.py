lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_cost = 0

for iteration in range(1, lost_fights + 1):
    if iteration % 2 == 0:
        total_cost += helmet_price
    if iteration % 3 == 0:
        total_cost += sword_price
    if iteration % 6 == 0:
        total_cost += shield_price
    if iteration % 12 == 0:
        total_cost += armor_price

print(f"Gladiator expenses: {total_cost:.2f} aureus")
