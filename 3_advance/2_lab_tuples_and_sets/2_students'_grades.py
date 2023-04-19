number_of_marks = int(input())
students_dict = {}

for mark in range(number_of_marks):
    student, new_mark = input().split()
    if student not in students_dict:
        students_dict[student] = []
    students_dict[student].append(float(new_mark))

for key in students_dict.keys():
    all_marks = [f"{grade:.2f}"for grade in students_dict[key]]
    print(f"{key} -> {' '.join(all_marks)} (avg: {sum(students_dict[key]) / len((students_dict[key])):.2f})")
