from collections import deque

tools = deque([int(x) for x in input().split(' ')])
substances = deque([int(x) for x in input().split(' ')])
challenges = [int(x) for x in input().split(' ')]

while tools and substances:

    current_substances = substances.pop()
    if current_substances <= 0:
        continue

    current_tool = tools.popleft()
    current_sum = current_tool * current_substances

    if current_sum in challenges:
        challenges.remove(current_sum)
        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            break
        continue

    # back of sq ?
    current_tool += 1
    tools.append(current_tool)

    current_substances -= 1
    substances.append(current_substances)

else:
    print("Harry is lost in the temple. Oblivion awaits him.")


if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
