
days_loop = int(input())
total_food = float(input())

dog_ate = 0
cat_ate = 0
biscuit = 0
total_ate_food = 0
dog_ate_total = 0
cat_ate_total = 0
full_total_ate = 0

for d in range(1, days_loop+1):
    dog_ate = int(input())
    cat_ate = int(input())
    total_ate_food = cat_ate + dog_ate
    if d % 3 == 0:
        biscuit = biscuit + total_ate_food * 0.1
    dog_ate_total += dog_ate
    cat_ate_total += cat_ate
    full_total_ate += total_ate_food

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{(full_total_ate / total_food) * 100:.2f}% of the food has been eaten.")
print(f"{dog_ate_total / full_total_ate * 100:.2f}% eaten from the dog.")
print(f"{cat_ate_total / full_total_ate * 100:.2f}% eaten from the cat.")
