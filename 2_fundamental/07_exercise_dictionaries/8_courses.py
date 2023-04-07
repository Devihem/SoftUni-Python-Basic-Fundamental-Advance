
courses_dict = {}
while True:
    system_input = input().split(" : ")
    if system_input[0] == "end":
        break
    course = system_input[0]
    name = system_input[1]

    if course not in courses_dict:
        courses_dict[course] = name
    else:
        courses_dict[course] += f"|{name}"


for course_print in courses_dict:
    course_students_list = courses_dict[course_print].split("|")
    print(f"{course_print}: {len(course_students_list)}")
    [print(f"-- {student}") for student in course_students_list]
