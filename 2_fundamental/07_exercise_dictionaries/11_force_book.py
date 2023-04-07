def command_straight_slash(force: str, user: str, force_dict: dict):
    if force_dict is None:
        force_dict = {}

    user_exist = user_existence_checker(user, force_dict)

    if user_exist:
        return force_dict
    else:
        if force not in force_dict:
            force_dict[force] = user
            return force_dict
        else:
            force_dict[force] = f"{force_dict[force]}--{user}"
            return force_dict


def command_arrow(force: str, user: str, force_dict: dict):
    if force_dict is None:
        force_dict = {}

    user_exist = user_existence_checker(user, force_dict)

    if user_exist:
        force_dict = user_side_switch(user, force_dict)
        if force not in force_dict:
            force_dict[force] = user
            print(f"{user} joins the {force} side!")
            return force_dict
        else:
            force_dict[force] = f"{force_dict[force]}--{user}"
            print(f"{user} joins the {force} side!")
            return force_dict
    else:
        if force not in force_dict:
            force_dict[force] = user
            print(f"{user} joins the {force} side!")
            return force_dict
        else:
            force_dict[force] = f"{force_dict[force]}--{user}"
            print(f"{user} joins the {force} side!")
            return force_dict


def user_existence_checker(user: str, force_dict: dict):
    for key in force_dict:
        for name in force_dict[key].split("--"):
            if name == user:
                return True
    return False


def user_side_switch(user: str, force_dict: dict):
    for key in force_dict:
        temporary_list = []
        for name in force_dict[key].split("--"):
            temporary_list.append(name)
        else:
            if user in temporary_list:
                temporary_list.remove(user)
                force_dict[key] = '--'.join(temporary_list)
                if force_dict[key] == '':
                    force_dict.pop(key)
                return force_dict
    return force_dict


force_sides_dict = {}
while True:

    system_input = input()
    if "Lumpawaroo" in system_input:
        break

    if "|" in system_input:
        force, user = system_input.split(" | ")
        force_sides_dict = command_straight_slash(force, user, force_sides_dict)
    elif "->" in system_input:
        user, force = system_input.split(" -> ")
        force_sides_dict = command_arrow(force, user, force_sides_dict)

for key_force in force_sides_dict:
    temporary_list_2 = force_sides_dict[key_force].split("--")
    if len(temporary_list_2) > 0:
        print(f"Side: {key_force}, Members: {len(temporary_list_2)}")
        [print(f"! {user_f}") for user_f in temporary_list_2]
