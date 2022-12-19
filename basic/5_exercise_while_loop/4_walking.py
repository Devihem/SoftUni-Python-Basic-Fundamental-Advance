today_steps = 0
goal_steps = 10000

while today_steps <= goal_steps:
    step_count = input()
    if step_count != "Going home":
        step_count = int(step_count)
        today_steps += step_count
    else:
        step_count = int(input())
        today_steps += step_count
        break

if today_steps >= goal_steps:
    print("Goal reached! Good job!")
    print(f"{today_steps - goal_steps} steps over the goal!")
elif today_steps < goal_steps:
    print(f"{goal_steps - today_steps} more steps to reach goal.")
