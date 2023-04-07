quantity = int(input())
days = int(input())
current_price = 0
current_spirit = 0

for d in range(1, days+1):
    if d % 11 == 0:
        quantity += 2

    tree_garland_and_skirt_bought = False
    if d % 2 == 0 and quantity > 0:
        # Ornament Set
        current_price += (2 * quantity)
        current_spirit += 5

    if d % 3 == 0 and quantity > 0:
        # Tree Garland and Tree Skirt
        current_price += ((5 + 3) * quantity)
        current_spirit += 3 + 10
        tree_garland_and_skirt_bought = True

    if d % 5 == 0 and quantity > 0:
        # Tree Lights
        current_price += (15 * quantity)
        current_spirit += 17
        if tree_garland_and_skirt_bought:
            current_spirit += 30

    if d % 10 == 0:
        #  cat ruined decoration
        current_price += 3 + 5 + 15
        current_spirit -= 20



if days > 0 and days % 10 == 0:
    current_spirit -= 30

print(f"Total cost: {current_price}")
print(f"Total spirit: {current_spirit}")
