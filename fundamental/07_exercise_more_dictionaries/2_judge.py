users_dictionary = {}
contest_order_list = []
while True:
    command = input()
    if command == "no more time":
        break
    user, contest, points = command.split(" -> ")
    if contest not in contest_order_list:
        contest_order_list.append(contest)
    if user not in users_dictionary:
        users_dictionary[user] = {}
    if contest not in users_dictionary[user].keys():
        users_dictionary[user][contest] = 0
    if int(points) > users_dictionary[user][contest]:
        users_dictionary[user][contest] = int(points)

course_dictionary = {}
for course in contest_order_list:
    course_dictionary[course] = {}
    for student in users_dictionary:
        for cont in users_dictionary[student].keys():
            if cont == course:
                if student not in course_dictionary[course]:
                    course_dictionary[course][student] = users_dictionary[student][course]

for course in contest_order_list:
    print(f"{course}: {len(course_dictionary[course])} participants")
    counter = 0
    sorted_score_list = []
    for item in course_dictionary[course]:
        sorted_score_list = sorted(course_dictionary[course].items(), key=lambda k: (-k[1], k[0]))
    for name_score in sorted_score_list:
        counter += 1
        score_user = name_score[0]
        score_points = name_score[1]
        print(f"{counter}. {score_user} <::> {score_points}")

total_score_dict = {}
for sum_score_user in users_dictionary:
    total_score_dict[sum_score_user] = (sum(users_dictionary[sum_score_user].values()))

total_score_list = sorted(total_score_dict.items(), key=lambda k: (-k[1], k[0]))
print("Individual standings:")
counter = 0
for list_user in total_score_list:
    counter += 1
    user_print = list_user[0]
    score_print = list_user[1]
    print(f"{counter}. {user_print} -> {score_print}")
