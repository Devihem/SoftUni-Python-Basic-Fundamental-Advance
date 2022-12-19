

d = int(input())
w = int(input())
h = int(input())
used_space = float(input())

aquarium_size = d*w*h
aquarium_size_DM = d*w*h/1000
water_liters=aquarium_size_DM

max_water = water_liters*(1-used_space/100)
print(max_water)


