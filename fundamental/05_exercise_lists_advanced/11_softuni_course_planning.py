schedule = input().split(", ")

while True:
    command = input().split(":")
    option = command[0]
    if option == "course start":
        break
    task = command[1]
    if option == "Add":
        if task not in schedule:
            schedule.append(task)

    elif option == "Insert":
        index = int(command[2])
        if task not in schedule:
            schedule.insert(index, task)

    elif option == "Remove":
        if task in schedule:
            schedule.remove(task)
            if task + "Exercise" in schedule:
                schedule.remove(task + "Exercise")

    elif option == "Swap":
        task_2 = command[2]
        if task in schedule and task_2 in schedule:
            index_1 = schedule.index(task)
            index_2 = schedule.index(task_2)
            schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]
            if task + "-Exercise" in schedule:
                temporary_box = schedule.pop(schedule.index(task + "-Exercise"))
                schedule.insert(schedule.index(task) + 1, temporary_box)
            if task_2 + "-Exercise" in schedule:
                temporary_box = schedule.pop(schedule.index(task_2 + "-Exercise"))
                schedule.insert(schedule.index(task_2) + 1, temporary_box)

    elif option == "Exercise":
        if task + "-Exercise" and task not in schedule:
            schedule.append(task)
            schedule.append(task + "-Exercise")
        elif task + "-Exercise" not in schedule:
            schedule.insert(schedule.index(task) + 1, task + "-Exercise")

schedule = [str(index + 1) + "." + item for index, item in enumerate(schedule)]
print("\n".join(schedule))
