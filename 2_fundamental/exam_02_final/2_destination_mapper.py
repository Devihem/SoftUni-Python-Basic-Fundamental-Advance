import re

map_string = input()
travel_list = []
travel_points = 0
pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, map_string)

for match in matches:
    travel_list.append(match[1])
    travel_points += len(match[1])

print(f"Destinations: {', '.join(travel_list)}")
print(f"Travel Points: {travel_points}")
