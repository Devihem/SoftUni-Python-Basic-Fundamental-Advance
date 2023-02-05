# Every value is - 1 unit / 1 hour
employee_1, employee_2, employee_3 = int(input()), int(input()), int(input())
students_questions_count = int(input())
total_employee_work_power = employee_1 + employee_2 + employee_3
needed_hours_work = 0
counter = 0
while students_questions_count > 0:

    students_questions_count -= total_employee_work_power
    needed_hours_work += 1
    counter += 1

    if students_questions_count > 0 and counter == 3:
        needed_hours_work += 1
        counter = 0

print(f"Time needed: {needed_hours_work}h.")
