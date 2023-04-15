from collections import deque
from datetime import datetime, timedelta


def robots_ended_work(working_robots_list: deque):
    looking_for_free_robots_list = deque([])
    for free_unit in range(len(working_robots_list)):
        checking_robot = working_robots_list.popleft()
        left_working_time = checking_robot[2]
        if left_working_time == 0:
            checking_robot.pop()
            looking_for_free_robots_list.append(checking_robot)
        else:
            working_robots_list.append(checking_robot)

    return looking_for_free_robots_list, working_robots_list


def working_robots_process(working_robots_list: deque):
    for unit in range(len(working_robots_list)):
        robot = working_robots_list.popleft()
        working_time = int(robot[2])
        working_time = working_time - 1
        robot[2] = working_time
        working_robots_list.append(robot)
    return working_robots_list


# Robots - Info Input
robots_info = [robot.split('-') for robot in input().split(";")]
robots_order_in_the_line = [robot_info[0] for robot_info in robots_info]

# Robot Free / Busy - List
free_robots = deque(robots_info)
working_robots = deque([])

# Starting Time
current_time = datetime.strptime(input(), '%H:%M:%S')
# Test Zone
product_line_queue = deque([])

# Product Input in Queue
while True:
    new_product = input()
    if new_product == "End":
        break
    product_line_queue.append(new_product)

while product_line_queue:
    current_time += timedelta(0, 1)
    next_item = product_line_queue.popleft()

    if free_robots:
        # Working process step by step
        free_robot_to_work = free_robots.popleft()
        print(f"{free_robot_to_work[0]} - {next_item}"
              f" [{current_time.strftime('%H:%M:%S')}]")
        robot_process_time = free_robot_to_work[1]
        free_robot_to_work.append(robot_process_time)
        working_robots.append(free_robot_to_work)

    else:
        product_line_queue.append(next_item)

    #   Processing the work by second
    working_robots = working_robots_process(working_robots)

    # Checking if robot is free
    new_free_robots, working_robots = robots_ended_work(working_robots)

    # Re-arrange the robots in the line ( fixing )
    if new_free_robots:
        new_reorder = []
        all_robots_free = free_robots + new_free_robots
        for robot_name in robots_order_in_the_line:
            for _ in range(len(all_robots_free)):
                robot_transfer = all_robots_free.popleft()
                if robot_transfer[0] == robot_name:
                    new_reorder.append(robot_transfer)
                else:
                    all_robots_free.append(robot_transfer)
        free_robots = deque(new_reorder)
