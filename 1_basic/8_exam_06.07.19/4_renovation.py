from math import ceil
height = int(input())
length = int(input())
no_painting_zone = int(input())

total_size = height * length * 4
area_for_painting = ceil(total_size - total_size * no_painting_zone / 100)
flag = True

while flag:
    work = input()
    if work == "Tired!":
        break
    else:
        work = int(work)
    area_for_painting -= work

    if area_for_painting <= 0:
        flag = False

if area_for_painting > 0:
    print(f"{area_for_painting} quadratic m left.")
elif area_for_painting == 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {-area_for_painting} l paint left!")
