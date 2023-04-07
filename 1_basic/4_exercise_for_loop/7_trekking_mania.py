groups_number_loop = int(input())
single_group_size = 0

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0


for i in range(0, groups_number_loop):
    single_group_size = int(input())

    if single_group_size <= 5:
        musala += single_group_size
    elif single_group_size <= 12:
        monblan += single_group_size
    elif single_group_size <= 25:
        kilimandjaro += single_group_size
    elif single_group_size <= 40:
        k2 += single_group_size
    elif single_group_size >= 41:
        everest += single_group_size

total_people = musala + monblan + kilimandjaro + k2 + everest
percent_sample = total_people / 100

print(f"{musala/percent_sample:.2f}%")
print(f"{monblan/percent_sample:.2f}%")
print(f"{kilimandjaro/percent_sample:.2f}%")
print(f"{k2/percent_sample:.2f}%")
print(f"{everest/percent_sample:.2f}%")