time_for_shots = int(input())
actions = int(input())
actions_time = int(input())

time_needed = time_for_shots * 0.15 + actions_time * actions

diff = abs(time_needed - time_for_shots)

if time_needed <= time_for_shots:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
elif time_needed > time_for_shots:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")
