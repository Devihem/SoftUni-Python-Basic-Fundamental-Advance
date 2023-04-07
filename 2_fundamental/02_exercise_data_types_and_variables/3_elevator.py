from math import ceil

people = int(input())
max_people_in_elevator = int(input())
courses = ceil(people / max_people_in_elevator)
print(courses)
