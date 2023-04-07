time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first+time_second+time_third

from_sec_to_min = total_time//60
sec_lefted = total_time%60

if sec_lefted <= 9:
    print(str(from_sec_to_min)+":0"+str(sec_lefted))
else:
    print(str(from_sec_to_min)+":"+str(sec_lefted))