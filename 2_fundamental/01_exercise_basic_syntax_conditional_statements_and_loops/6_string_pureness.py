string_loops = int(input())

for string in range(0, string_loops):
    new_string = input()

    if "," in new_string or "." in new_string or "_" in new_string:
        print(f"{new_string} is not pure!")
    else:
        print(f"{new_string} is pure.")
