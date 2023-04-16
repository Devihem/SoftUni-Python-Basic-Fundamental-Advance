from collections import deque

cups = deque([int(cup) for cup in input().split()])
bottles = deque([int(bottle) for bottle in input().split()])
wasted_water = 0

while bottles and cups:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    while current_cup > 0:
        current_cup = current_cup - current_bottle

        if current_cup > 0 and bottles:
            current_bottle = bottles.pop()
        elif current_cup < 0:
            wasted_water += current_cup
        else:
            break
else:
    if not cups:
        print(f"Bottles: ", end="")
        print(*bottles)
    elif not bottles:
        print(f"Cups: ", end="")
        print(*cups)

print(f"Wasted litters of water: {wasted_water * -1}")
