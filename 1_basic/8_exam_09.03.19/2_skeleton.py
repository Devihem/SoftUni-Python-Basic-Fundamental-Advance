minuets_time = int(input())
seconds_time = int(input())
distance_m = float(input())
sec_for_100m = int(input())

target_time_in_sec = minuets_time * 60 + seconds_time

track_time = ((distance_m / 100) * sec_for_100m) - ((distance_m / 120) * 2.5)

if target_time_in_sec >= track_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {track_time:.3f}.")
elif target_time_in_sec < track_time:
    print(f"No, Marin failed! He was {track_time - target_time_in_sec:.3f} second slower.")
