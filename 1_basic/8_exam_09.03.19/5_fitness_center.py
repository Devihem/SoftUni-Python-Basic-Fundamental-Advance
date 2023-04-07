people = int(input())

back = 0
chest = 0
legs = 0
abs = 0
p_shake = 0
p_bar = 0
counter = 0

while counter < people:

    counter += 1
    activity = input()

    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        p_shake += 1
    elif activity == "Protein bar":
        p_bar += 1

group_training = back + chest + legs + abs
group_protein = p_bar + p_shake

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{p_shake} - protein shake")
print(f"{p_bar} - protein bar")
print(f"{group_training / people * 100:.2f}% - work out")
print(f"{group_protein / people * 100:.2f}% - protein")
