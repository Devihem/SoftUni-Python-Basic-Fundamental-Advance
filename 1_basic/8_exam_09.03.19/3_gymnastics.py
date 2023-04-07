country = input()
sport_type = input()
points_level = 0
points_performance = 0


if country == "Russia":
    if sport_type == "ribbon":
        points_level = 9.1
        points_performance = 9.4
    elif sport_type == "hoop":
        points_level = 9.3
        points_performance = 9.8
    elif sport_type == "rope":
        points_level = 9.6
        points_performance = 9

if country == "Bulgaria":
    if sport_type == "ribbon":
        points_level = 9.6
        points_performance = 9.4
    elif sport_type == "hoop":
        points_level = 9.55
        points_performance = 9.75
    elif sport_type == "rope":
        points_level = 9.5
        points_performance = 9.4

if country == "Italy":
    if sport_type == "ribbon":
        points_level = 9.2
        points_performance = 9.5
    elif sport_type == "hoop":
        points_level = 9.45
        points_performance = 9.35
    elif sport_type == "rope":
        points_level = 9.7
        points_performance = 9.15

total = points_level + points_performance

print(f"The team of {country} get {total:.3f} on {sport_type}.")
print(f"{100 - (total / 20) * 100:.2f}%")
