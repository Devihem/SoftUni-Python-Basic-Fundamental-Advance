# sloppy solved
def list_manipulator(numbers_list, add_remove_command, beginning_end_command, *parameters):
    parameters_list = list(parameters)
    if add_remove_command == 'add':
        if beginning_end_command == 'beginning':
            parameters_list.extend(numbers_list)
            return parameters_list
        else:
            numbers_list.extend(parameters_list)
            return numbers_list
    else:
        if not parameters_list:
            remove_count = 1
        else:
            remove_count = parameters_list[0]
        if beginning_end_command == 'beginning':
            numbers_list = numbers_list[remove_count:]
        else:
            numbers_list = numbers_list[:-remove_count]
        return numbers_list
