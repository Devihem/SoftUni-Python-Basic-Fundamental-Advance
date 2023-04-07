people_order_list = input().split()
skipped_people_factor = int(input())
counter = 0
removed_people_list = []

while len(people_order_list) > 0:
    for index, people in enumerate(people_order_list):
        counter += 1
        if counter == skipped_people_factor:
            removed_people_list.append(people)
            people_order_list[index] = "-"
            counter = 0

    while "-" in people_order_list:
        people_order_list.remove("-")

print("[", end="")
print(*removed_people_list, sep=",", end="")
print("]")
