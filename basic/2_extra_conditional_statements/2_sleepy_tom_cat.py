free_days = int(input())
working_days = 365-free_days

free_days_play_time = 127
working_days_play_time = 63

total_play_time = working_days*working_days_play_time+free_days_play_time*free_days
maximum_wanted_play_time = 30000

deff = abs(maximum_wanted_play_time-total_play_time)
hours = deff//60
minuets = deff%60



if total_play_time > maximum_wanted_play_time:
    print("Tom will run away")
    print(f"{hours} hours and {minuets} minutes more for play")
elif total_play_time < maximum_wanted_play_time:
    print("Tom sleeps well")
    print(f"{hours} hours and {minuets} minutes less for play")