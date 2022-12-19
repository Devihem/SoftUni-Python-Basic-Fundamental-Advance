max_fails = int(input())
current_fails = 0
score = 0
total_score = 0
task_count = 0


while max_fails > current_fails:
    task_name = input()
    if task_name == "Enough":
        print(f"Average score: {total_score/task_count:.2f}")
        print(f"Number of problems: {task_count}")
        print(f"Last problem: {last_task_name}")
        break
    score = int(input())
    total_score += score
    task_count += 1
    last_task_name = task_name
    if score <= 4:
        current_fails += 1

else:
    print(f"You need a break, {current_fails} poor grades.")
