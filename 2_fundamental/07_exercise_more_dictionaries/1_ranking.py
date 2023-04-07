course_password_dict = {}
contest_dict = {}
ranking_dict = {}
while True:
    command_task_one = input().split(":")
    if command_task_one[0] == "end of contests":
        break
    key = command_task_one[0]
    password = command_task_one[1]
    course_password_dict[key] = password

while True:
    command_task_two = input().split("=>")
    if command_task_two[0] == "end of submissions":
        break
    contest = command_task_two[0]
    password = command_task_two[1]
    username = command_task_two[2]
    points = int(command_task_two[3])
    if contest in course_password_dict.keys():
        if course_password_dict[contest] == password:
            if username not in contest_dict.keys():
                contest_dict[username] = {}

            if contest in contest_dict[username].keys():
                if points > contest_dict[username][contest]:
                    contest_dict[username][contest] = points
            else:
                contest_dict[username][contest] = points

for key in contest_dict:
    ranking_dict[key] = sum(contest_dict[key].values())

max_score = (max(ranking_dict, key=ranking_dict.get))

print(f"Best candidate is {max_score} with total {ranking_dict[max_score]} points.")
print("Ranking:")

alphabetic_order_dict = sorted(contest_dict)

for user in alphabetic_order_dict:
    print(user)
    sorted_score = sorted(contest_dict[user], key=contest_dict[user].get, reverse=True)
    for course in sorted_score:
        print(f"#  {course} -> {contest_dict[user][course]}")
