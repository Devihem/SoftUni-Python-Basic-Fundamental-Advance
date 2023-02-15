number_of_cycles = int(input())
students_score_dict = {}
for _ in range(number_of_cycles):
    student_name = input()
    if student_name not in students_score_dict:
        students_score_dict[student_name] = float(input())
    else:
        student_score = float(input())
        students_score_dict[student_name] = (students_score_dict[student_name] + student_score) / 2

students_score_dict = {name: students_score_dict[name] for name in students_score_dict if
                       students_score_dict[name] >= 4.5}

[print(f"{student} -> {students_score_dict[student]:.2f}") for student in students_score_dict]
