from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
paper = deque([int(x) for x in input().split(', ')])
total_boxes = 0

while eggs and paper:

    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue
    if current_egg == 13:
        first_paper = paper.popleft()
        last_paper = paper.pop()
        paper.append(first_paper)
        paper.appendleft(last_paper)
        continue

    current_paper = paper.pop()

    current_sum = current_paper + current_egg

    if current_sum <= 50:
        total_boxes += 1
        continue

if total_boxes > 0:
    print(f"Great! You filled {total_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")

if paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper])}")