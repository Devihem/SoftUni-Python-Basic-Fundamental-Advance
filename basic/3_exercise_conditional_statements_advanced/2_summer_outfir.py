temperature_c = int(input())
time_of_day = input()

outfit = 0
shoes = 0

if time_of_day == "Morning":
    if 10 <= temperature_c <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < temperature_c <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temperature_c >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif time_of_day == "Afternoon":
    if 10 <= temperature_c <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temperature_c <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif temperature_c >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif time_of_day == "Evening":
    if 10 <= temperature_c <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temperature_c <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temperature_c >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temperature_c} degrees, get your {outfit} and {shoes}.")
