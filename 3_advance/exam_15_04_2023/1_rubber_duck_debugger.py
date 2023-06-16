from collections import deque

time = deque([int(x) for x in input().split(' ')])
task = deque([int(x) for x in input().split(' ')])

ducky_dict = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,
}
while time and task:

    current_time = time.popleft()
    current_task = task.pop()
    current_sum = current_task * current_time

    if current_sum > 240:

        time.append(current_time)
        task.append(current_task - 2)

    elif 0 <= current_sum <= 240:

        if current_sum <= 60:
            ducky_dict['Darth Vader Ducky'] += 1

        elif current_sum <= 120:
            ducky_dict['Thor Ducky'] += 1

        elif current_sum <= 180:
            ducky_dict['Big Blue Rubber Ducky'] += 1

        else:
            ducky_dict['Small Yellow Rubber Ducky'] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f'{duck}: {count}') for duck, count in ducky_dict.items()]
