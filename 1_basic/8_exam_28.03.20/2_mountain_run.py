from math import floor
world_record = float(input())
distance = float(input())
time_sec_for_1m = float(input())

slowdown_time = floor(distance / 50) * 30
total_time_sec = distance * time_sec_for_1m + slowdown_time

if total_time_sec < world_record:
    print(f"Yes! The new record is {total_time_sec:.2f} seconds.")
else:
    print(f"No! He was {total_time_sec - world_record:.2f} seconds slower.")