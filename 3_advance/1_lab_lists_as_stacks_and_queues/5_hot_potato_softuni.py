from _collections import deque

kids_circle = deque(input().split())
hot_potato_index = int(input())
new_circle = []
counter = 0

while len(kids_circle) > 1:
    counter += 1
    if counter == hot_potato_index:
        removed_kid = kids_circle.popleft()
        counter = 0
        print(f"Removed {removed_kid}")
    else:
        kids_circle.append(kids_circle.popleft())
else:
    print(f"Last is {kids_circle[0]}")
