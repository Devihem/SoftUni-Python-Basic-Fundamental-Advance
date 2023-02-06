from math import ceil

number_of_students = int(input())
number_of_lecture = int(input())
additional_bonus = int(input())
maximum_attendance = 0

for student in range(number_of_students):
    student_attendance = float(input())
    if student_attendance > maximum_attendance:
        maximum_attendance = student_attendance
if number_of_lecture == 0:
    maximum_bonus_point = 0
else:
    maximum_bonus_point = maximum_attendance / number_of_lecture * (5 + additional_bonus)

print(f"Max Bonus: {ceil(maximum_bonus_point)}.")
print(f"The student has attended {maximum_attendance:.0f} lectures.")
