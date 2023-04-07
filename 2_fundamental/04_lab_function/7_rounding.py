numbers_list = input().split()
reworked_list = []

for item in numbers_list:
    item = round(float(item))
    reworked_list.append(item)

print(reworked_list)
