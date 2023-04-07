def command_move(shifted_numbers: int, encrypted_list: list):
    shifted_symbols = encrypted_list[:shifted_numbers]
    encrypted_list = encrypted_list[shifted_numbers:] + shifted_symbols
    return encrypted_list


def command_insert(insert_index: int, insert_value: str, encrypted_list: list):
    insert_list = list(insert_value)
    encrypted_list = encrypted_list[:insert_index] + insert_list + encrypted_list[insert_index:]
    return encrypted_list


def command_change(old_text: str, replacement_text: str, encrypted_list: list):
    current_string_encrypted = ''.join(encrypted_list)
    if old_text == replacement_text:
        return encrypted_list
    current_string_encrypted = current_string_encrypted.replace(old_text, replacement_text)
    encrypted_list = list(current_string_encrypted)
    return encrypted_list


coded_message_list = list(input())

while True:
    system_input = input()

    if system_input == "Decode":
        print(f"The decrypted message is: {''.join(coded_message_list)}")
        break

    command = system_input.split("|")

    if command[0] == "Move":
        coded_message_list = command_move(int(command[1]), coded_message_list)
    elif command[0] == "Insert":
        coded_message_list = command_insert(int(command[1]), command[2], coded_message_list)
    elif command[0] == "ChangeAll":
        coded_message_list = command_change(command[1], command[2], coded_message_list)
