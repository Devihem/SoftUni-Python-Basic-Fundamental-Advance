total_ships_destroyed = 0
battlefield = []
battlefield_rows = int(input())
for row in range(battlefield_rows):
    battlefield.append(input().split(" "))

attack_plan = input().split(" ")

for attack in attack_plan:
    row, col = attack.split("-")
    row = int(row)
    col = int(col)
    if int(battlefield[row][col]) > 0:
        battlefield[row][col] = str((int(battlefield[row][col]) - 1))
        if battlefield[row][col] == "0":
            total_ships_destroyed += 1

print(total_ships_destroyed)
