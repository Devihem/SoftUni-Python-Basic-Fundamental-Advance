season = input()
group_type = input()
students_number = int(input())
nights_staying = int(input())

sport = 0
discount = 1
price = 0

if group_type == "boys":
    if season == "Winter":
        sport = "Judo"
        price = 9.60
    elif season == "Spring":
        sport = "Tennis"
        price = 7.20
    elif season == "Summer":
        sport = "Football"
        price = 15

if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
        price = 9.60
    elif season == "Spring":
        sport = "Athletics"
        price = 7.20
    elif season == "Summer":
        sport = "Volleyball"
        price = 15

if group_type == "mixed":
    if season == "Winter":
        sport = "Ski"
        price = 10
    elif season == "Spring":
        sport = "Cycling"
        price = 9.50
    elif season == "Summer":
        sport = "Swimming"
        price = 20

if students_number >= 50:
    discount = 0.5
elif 20 <= students_number < 50:
    discount = 0.85
elif 10 <= students_number < 20:
    discount = 0.95

end_sum = students_number * price * nights_staying * discount

print(f"{sport} {end_sum:.2f} lv.")
