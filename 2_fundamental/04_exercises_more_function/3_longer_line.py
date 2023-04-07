from math import floor


def distance_from_point_to_point_4_3(x1_value, y1_value, x2_value, y2_value):
    first_dot_distance = distance_from_center_4_2(x1_value, y1_value)
    second_dot_distance = distance_from_center_4_2(x2_value, y2_value)
    if first_dot_distance > second_dot_distance:
        return (x2_value - x1_value) ** 2 + (y2_value - y1_value) ** 2
    elif second_dot_distance >= first_dot_distance:
        return (x1_value - x2_value) ** 2 + (y1_value - y2_value) ** 2


def distance_from_center_4_2(x_value, y_value):
    return x_value ** 2 + y_value ** 2


x1_number, y1_number, x2_number, y2_number = float(input()), float(input()), float(input()), float(input())
x3_number, y3_number, x4_number, y4_number = float(input()), float(input()), float(input()), float(input())



line_1 = distance_from_point_to_point_4_3(x1_number, y1_number, x2_number, y2_number)
line_2 = distance_from_point_to_point_4_3(x3_number, y3_number, x4_number, y4_number)


if line_2 > line_1:
    dot_1_to_center = distance_from_center_4_2(x3_number, y3_number)
    dot_2_to_center = distance_from_center_4_2(x4_number, y4_number)

    if dot_1_to_center > dot_2_to_center:
        the_closer_dot = f"({floor(x4_number)}, {floor(y4_number)})"
        the_far_dot = f"({floor(x3_number)}, {floor(y3_number)})"
        print(f"{the_closer_dot}{the_far_dot}")
    elif dot_2_to_center >= dot_1_to_center:
        the_closer_dot = f"({floor(x3_number)}, {floor(y3_number)})"
        the_far_dot = f"({floor(x4_number)}, {floor(y4_number)})"
        print(f"{the_closer_dot}{the_far_dot}")



elif line_1 >= line_2:
    dot_1_to_center = distance_from_center_4_2(x1_number, y1_number)
    dot_2_to_center = distance_from_center_4_2(x2_number, y2_number)

    if dot_1_to_center > dot_2_to_center:
        the_closer_dot = f"({floor(x2_number)}, {floor(y2_number)})"
        the_far_dot = f"({floor(x1_number)}, {floor(y1_number)})"
        print(f"{the_closer_dot}{the_far_dot}")
    elif dot_2_to_center >= dot_1_to_center:
        the_closer_dot = f"({floor(x1_number)}, {floor(y1_number)})"
        the_far_dot = f"({floor(x2_number)}, {floor(y2_number)})"
        print(f"{the_closer_dot}{the_far_dot}")
