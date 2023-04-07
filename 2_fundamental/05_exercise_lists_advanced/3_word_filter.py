even_food_list = [food for food in input().split() if len(food) % 2 == 0]
print(*even_food_list, sep="\n")
