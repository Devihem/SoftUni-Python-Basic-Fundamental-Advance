clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
new_rack_capacity = rack_capacity
racks_used_total = 1

for _ in range(len(clothes)):
    new_clothe = clothes.pop()
    if new_rack_capacity - new_clothe < 0:
        racks_used_total += 1
        new_rack_capacity = rack_capacity
    new_rack_capacity -= new_clothe

print(racks_used_total)
