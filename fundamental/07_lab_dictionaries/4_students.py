students_dict = {}
current_course = ""
while True:
    system_input = input().split(":")
    if system_input[0][0].isupper():
        students_dict[system_input[1]] = system_input[0], system_input[2]
    else:
        current_course = ' '.join(system_input[0].split("_"))
        break

for key in students_dict:
    if students_dict[key][1] == current_course:
        print(f"{students_dict[key][0]} - {key}")
