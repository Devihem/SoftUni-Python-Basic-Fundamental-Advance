from collections import deque


def working_clock(time_list):
    time_list[2] += 1
    if time_list[2] == 60:
        time_list[2] = 0
        time_list[1] += 1
        if time_list[1] == 60:
            time_list[1] = 0
            time_list[0] += 1
    return time_list


# Robots - Stacks  Free and Working
robots = input().split(";")
robots_info = [robot.split('-') for robot in robots]

free_robots = deque(robots_info)
working_robots = []

starting_time = [int(x) for x in input().split(":")]
product_line_queue = ["detail", "detail", "detail", "detail", "detail", "detail", "detail", "detail", "detail",
                      "detail", "detail", "detail"]

product = ""

while product != "End" or len(product_line_queue) >= 1:

    current_time = working_clock(starting_time)
    product_line_queue.pop()
    if product == "End":
        continue
    else:
        product = input()

    print(current_time)
    print(product_line_queue)
