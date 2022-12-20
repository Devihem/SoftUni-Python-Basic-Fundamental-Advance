companions = int(input())
days = int(input())
total_money = 0

for day in range(1, days+1):
    total_money += 50

    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5

    food_cost = 2 * companions
    total_money -= food_cost

    if day % 3 == 0:
        motivational_party = 3 * companions
        total_money -= motivational_party
    if day % 5 == 0:
        boss_slay_reward = 20 * companions
        total_money += boss_slay_reward
        if day % 3 == 0:
            motivational_party_extra = 2 * companions
            total_money -= motivational_party_extra

coins_per_companion = int(total_money / companions)
print(f"{companions} companions received {coins_per_companion} coins each.")
