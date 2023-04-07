games_sell_loop = int(input())
hearthstone_counter = 0
fortnite_counter = 0
overwatch_counter = 0
others_counter = 0
for i in range(0, games_sell_loop):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone_counter += 1
    elif game_name == "Fornite":
        fortnite_counter += 1
    elif game_name == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1

print(f"Hearthstone - {hearthstone_counter/games_sell_loop*100:.2f}%")
print(f"Fornite - {fortnite_counter/games_sell_loop*100:.2f}%")
print(f"Overwatch - {overwatch_counter/games_sell_loop*100:.2f}%")
print(f"Others - {others_counter/games_sell_loop*100:.2f}%")
