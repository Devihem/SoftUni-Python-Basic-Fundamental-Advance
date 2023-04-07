easter_breads_loop = int(input())
new_total_score = 0
best_total_score = 0
client_score = 0
best_baker = ""
for i in range(0, easter_breads_loop):
    baker_name = input()
    while True:
        client_score = input()
        if client_score == "Stop":
            print(f"{baker_name} has {new_total_score} points.")
            break
        else:
            client_score = int(client_score)
        new_total_score += client_score

    if new_total_score > best_total_score:
        print(f"{baker_name} is the new number 1!")
        best_total_score = new_total_score
        best_baker = baker_name

    new_total_score = 0

print(f"{best_baker} won competition with {best_total_score} points!")
