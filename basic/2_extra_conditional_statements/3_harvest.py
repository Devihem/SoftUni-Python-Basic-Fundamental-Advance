import math
vineyard_sqr_m = int(input())
grape_production = float(input())
wine_needed_litters = int(input())
workers = int(input())

grape_production_sqr_m = vineyard_sqr_m*0.40
grape_kg = grape_production_sqr_m*grape_production

wine_litters_production = grape_kg/2.5

deff = abs(wine_litters_production-wine_needed_litters)




if wine_litters_production < wine_needed_litters:
    print(f"It will be a tough winter! More {math.floor(deff)} liters wine needed.")
elif wine_litters_production >= wine_needed_litters:
    print(f"Good harvest this year! Total wine: {math.floor(wine_litters_production)} liters.")
    print(f"{math.ceil(deff)} liters left -> {math.ceil(deff/workers)} liters per person.")