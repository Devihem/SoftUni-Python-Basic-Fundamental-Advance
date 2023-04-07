movie_name = input()
zone_type = input()
tickets = int(input())

price = 0

if movie_name == "A Star Is Born":
    if zone_type == "normal":
        price = 7.50
    elif zone_type == "luxury":
        price = 10.50
    elif zone_type == "ultra luxury":
        price = 13.50
elif movie_name == "Bohemian Rhapsody":
    if zone_type == "normal":
        price = 7.35
    elif zone_type == "luxury":
        price = 9.45
    elif zone_type == "ultra luxury":
        price = 12.75
elif movie_name == "Green Book":
    if zone_type == "normal":
        price = 8.15
    elif zone_type == "luxury":
        price = 10.25
    elif zone_type == "ultra luxury":
        price = 13.25
elif movie_name == "The Favourite":
    if zone_type == "normal":
        price = 8.75
    elif zone_type == "luxury":
        price = 11.55
    elif zone_type == "ultra luxury":
        price = 13.95

total = tickets * price

print(f"{movie_name} -> {total:.2f} lv.")
