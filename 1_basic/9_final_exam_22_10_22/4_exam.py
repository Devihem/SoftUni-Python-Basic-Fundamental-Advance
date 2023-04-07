students_unit_loop = int(input())
mark = 0
group_1_counter = 0
group_2_counter = 0
group_3_counter = 0
group_4_counter = 0

total = 0

for i in range(0, students_unit_loop):
    mark = float(input())
    if mark < 3:
        group_1_counter += 1
    elif 3 <= mark < 4:
        group_2_counter += 1
    elif 4 <= mark < 5:
        group_3_counter += 1
    elif mark >= 5:
        group_4_counter += 1
    total += mark

print(f"Top students: {group_4_counter / students_unit_loop * 100:.2f}%")
print(f"Between 4.00 and 4.99: {group_3_counter / students_unit_loop * 100:.2f}%")
print(f"Between 3.00 and 3.99: {group_2_counter / students_unit_loop * 100:.2f}%")
print(f"Fail: {group_1_counter / students_unit_loop * 100:.2f}%")
print(f"Average: {total / students_unit_loop:.2f}")
