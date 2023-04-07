def register_option(car_number: str, user: str, reg_dict: dict):
    if user not in reg_dict:
        reg_dict[user] = car_number
        print(f"{user} registered {car_number} successfully")
    else:
        print(f"ERROR: already registered with plate number {car_number}")
    return plate_numbers_reg_dict


def unregister_option(user: str, reg_dict: dict):
    if user not in reg_dict:
        print(f"ERROR: user {user} not found")
    else:
        plate_numbers_reg_dict.pop(user)
        print(f"{user} unregistered successfully")
    return plate_numbers_reg_dict


loop_range = int(input())
plate_numbers_reg_dict = {}

for _ in range(loop_range):
    system_input = input().split()
    command = system_input[0]
    user_name = system_input[1]

    if command == "register":
        plate_number = system_input[2]
        plate_numbers_reg_dict = register_option(plate_number, user_name, plate_numbers_reg_dict)

    elif command == "unregister":
        plate_numbers_reg_dict = unregister_option(user_name, plate_numbers_reg_dict)

[print(f"{plate_numb} => {plate_numbers_reg_dict[plate_numb]}") for plate_numb in plate_numbers_reg_dict]
