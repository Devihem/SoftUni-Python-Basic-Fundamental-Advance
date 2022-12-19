from math import ceil
easter_breads = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0

for i in range(0, easter_breads):
    used_sugar = int(input())
    used_flour = int(input())
    total_sugar += used_sugar
    total_flour += used_flour
    if max_sugar < used_sugar:
        max_sugar = used_sugar
    if max_flour < used_flour:
        max_flour = used_flour

sugar_packs = ceil(total_sugar / 950)
flour_packs = ceil(total_flour / 750)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
