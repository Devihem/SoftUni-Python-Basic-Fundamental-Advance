def command_path_4_1(d_command, d_command_value):
    if d_command == "int":
        d_command_value = int(d_command_value)
        print(f"{d_command_value * 2}")
    elif d_command == "real":
        d_command_value = float(d_command_value)
        print(f"{d_command_value * 1.5:.2f}")
    elif d_command == "string":
        print(f"${d_command_value}$")


command = input()
command_value = input()
command_path_4_1(command, command_value)