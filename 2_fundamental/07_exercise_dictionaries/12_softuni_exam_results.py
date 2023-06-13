def judge_score_system(user: str, program: str, points: int, program_dict: dict):
    if program not in program_dict:
        program_dict[program] = f"{user}-{points}"
    else:
        program_dict[program] = f"{program_dict[program]}|{user}-{points}"

    return program_dict


def ban_user(banned_user: list, program_dict: dict):
    for key in program_dict:
        temporary_list = program_dict[key].split('|')
        temporary_list_2 = []
        for item in temporary_list:
            item = item.split('-')
            user = item[0]
            score = item[1]
            if user not in banned_user:
                temporary_list_2.append(f"{user}-{score}")
        program_dict[key] = '|'.join(temporary_list_2)
    return program_dict


def result_filter(program_dict: dict):
    for key in program_dict:
        temporary_list = program_dict[key].split('|')
        temporary_dict = {}
        if len(program_dict[key]) > 0:
            for item in temporary_list:
                item = item.split('-')
                user = item[0]
                score = item[1]
                if user not in temporary_dict:
                    temporary_dict[user] = score
                else:
                    if int(score) > int(temporary_dict[user]):
                        temporary_dict[user] = score
            program_dict[key] = temporary_dict
    return program_dict


def submission_counter(program_dict: dict):
    filtered_list = []
    for key in program_dict:
        filtered_list.append(f"{key} - {len(program_dict[key].split('|'))}")

    return filtered_list


score_dict = {}
banned_users_list = []
while True:

    system_input = input()
    if system_input == "exam_00_06_2020 finished":
        break
    elif "banned" in system_input:
        system_input = system_input.split("-")
        banned_users_list.append(system_input[0])
    else:
        system_input = system_input.split("-")
        name = system_input[0]
        language = system_input[1]
        scores = int(system_input[2])
        score_dict = judge_score_system(name, language, scores, score_dict)

submissions = submission_counter(score_dict.copy())
score_dict = ban_user(banned_users_list, score_dict)
users_filter = result_filter(score_dict.copy())

print("Results:")
[[print(f"{user_now} | {users_filter[program][user_now]}")
  for user_now in users_filter[program]]
 for program in users_filter]
print("Submissions:")
print('\n'.join(submissions))
