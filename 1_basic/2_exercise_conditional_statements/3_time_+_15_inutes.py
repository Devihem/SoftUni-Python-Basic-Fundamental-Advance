hours = int(input())
min = int(input())

re_timing = hours*60+min+15

new_hours = re_timing // 60
if new_hours >= 24:
    new_hours = new_hours-24

new_min = re_timing % 60

if new_min < 10:
    print(f"{new_hours}:0{new_min}")
else:
    print(f"{new_hours}:{new_min}")