size_x = float(input())
size_y = float(input())
size_h = float(input())


base_1 = size_x*size_x*2
door = 1.2*2
base_2 = size_x*size_y*2
windows = 1.5*1.5

base_area = base_1-door+base_2-windows*2

side_1 = (size_x*size_h/2)*2
side_2 = size_y * size_x*2
roof_area = side_1+side_2


needed_green_paint = base_area/3.4

needed_red_paint = roof_area/4.3

print(f"{needed_green_paint:.2f}")
print(f"{needed_red_paint:.2f}")
