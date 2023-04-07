racers_track_list = input().split()

first_racer_time = 0
second_racer_time = 0

for value_racer_1 in range(0, int((len(racers_track_list)-1)/2)):
    if int(racers_track_list[value_racer_1]) == 0:
        first_racer_time *= 0.8
    else:
        first_racer_time += int(racers_track_list[value_racer_1])

for value_racer_2 in range(len(racers_track_list)-1, int((len(racers_track_list)-1)/2), -1):
    if int(racers_track_list[value_racer_2]) == 0:
        second_racer_time *= 0.8
    else:
        second_racer_time += int(racers_track_list[value_racer_2])

if first_racer_time < second_racer_time:
    print(f"The winner is left with total time: {first_racer_time:.1f}")
elif second_racer_time < first_racer_time:
    print(f"The winner is right with total time: {second_racer_time:.1f}")
