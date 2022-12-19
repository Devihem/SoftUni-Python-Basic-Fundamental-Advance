student_name = input()

student_class = 0
total_sum = 0
fails = 0
while student_class < 12:
    year_grade = float(input())
    student_class += 1
    if year_grade < 4.00:
        fails += 1
        if fails > 1:
            print(f"{student_name} has been excluded at {student_class} grade")
            break
        student_class -= 1
        continue

    total_sum += year_grade

average = total_sum / 12
if student_class == 12 :
    print(f"{student_name} graduated. Average grade: {average:.2f}")
