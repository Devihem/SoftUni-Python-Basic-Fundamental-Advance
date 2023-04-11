kids_circle = input().split()
hot_potato_index = int(input())
new_circle = []
counter = 0

# hotpotato simulation
while len(kids_circle) > 1:
    counter += 1
    if counter == hot_potato_index:
        removed_kid = kids_circle.pop(0)
        counter = 0
        print(f"Removed {removed_kid}")
    else:
        kids_circle.append(kids_circle.pop(0))
else:
    print(f"Last is {kids_circle[0]}")
