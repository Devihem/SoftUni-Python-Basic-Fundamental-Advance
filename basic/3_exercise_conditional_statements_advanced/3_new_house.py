flower_types = input()
number_flowers = int(input())
money = int(input())

roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.5
total_sum = 0

if flower_types == "Roses":
    if number_flowers > 80:
        total_sum = roses * number_flowers * 0.9
    else:
        total_sum = roses * number_flowers

if flower_types == "Dahlias":
    if number_flowers > 90:
        total_sum = dahlias * number_flowers * 0.85
    else:
        total_sum = dahlias * number_flowers

if flower_types == "Tulips":
    if number_flowers > 80:
        total_sum = tulips * number_flowers * 0.85
    else:
        total_sum = tulips * number_flowers

if flower_types == "Narcissus":
    if number_flowers < 120:
        total_sum = narcissus * number_flowers * 1.15
    else:
        total_sum = narcissus * number_flowers

if flower_types == "Gladiolus":
    if number_flowers < 80:
        total_sum = gladiolus * number_flowers * 1.20
    else:
        total_sum = gladiolus * number_flowers

diff = abs(money - total_sum)

if money >= total_sum:
    print(f"Hey, you have a great garden with {number_flowers} {flower_types} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
