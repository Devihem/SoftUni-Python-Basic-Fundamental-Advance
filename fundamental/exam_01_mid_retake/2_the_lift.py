people = int(input())
lift_wagon_list = [int(number) for number in input().split()]

for index, wagon in enumerate(lift_wagon_list):
    while lift_wagon_list[index] < 4:
        if people == 0:
            break
        lift_wagon_list[index] += 1
        people -= 1

if people == 0 and sum(lift_wagon_list) == len(lift_wagon_list) * 4:
    print(*lift_wagon_list)
elif people == 0:
    lift_wagon_list = [str(value) for value in lift_wagon_list]
    print(f"The lift has empty spots!\n{' '.join(lift_wagon_list)}")
else:
    lift_wagon_list = [str(value) for value in lift_wagon_list]
    print(f"There isn't enough space! {people} people in a queue!\n{' '.join(lift_wagon_list)}")
