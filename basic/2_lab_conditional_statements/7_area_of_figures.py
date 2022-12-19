import math

fig = input()

if fig in ["square"]:
    square_side = float(input())
    square_area = square_side*square_side
    print(f"{square_area:.3f}")
elif fig in ["rectangle"]:
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    rectangle_area = rectangle_side_b * rectangle_side_a
    print(f"{rectangle_area:.3f}")
elif fig in ["circle"]:
    circle_radios = float(input())
    circle_area = math.pi*circle_radios**2
    print(f"{circle_area:.3f}")
elif fig in ["triangle"]:
    triangle_side = float(input())
    triangle_high = float(input())
    triangle_area = triangle_high*triangle_side/2
    print(f"{triangle_area:.3f}")