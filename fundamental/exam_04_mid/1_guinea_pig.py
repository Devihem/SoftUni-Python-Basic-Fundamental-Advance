food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000
day = 0

for days in range(1, 30+1):
    food -= 300
    if days % 2 == 0:
        hay -= food*0.05
    if days % 3 == 0:
        cover -= guinea_pig_weight/3
    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
