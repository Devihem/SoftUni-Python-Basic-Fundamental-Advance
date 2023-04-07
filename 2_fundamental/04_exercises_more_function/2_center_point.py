from math import floor
def distance_from_center_4_2(x_value, y_value):
    return x_value ** 2 + y_value ** 2


x1_number, y1_number, x2_number, y2_number = float(input()), float(input()), float(input()), float(input())

first_dot_distance = distance_from_center_4_2(x1_number, y1_number)
second_dot_distance = distance_from_center_4_2(x2_number, y2_number)

if first_dot_distance > second_dot_distance:
    print(f"({floor(x2_number)}, {floor(y2_number)})")
elif second_dot_distance >= first_dot_distance:
    print(f"({floor(x1_number)}, {floor(y1_number)})")
