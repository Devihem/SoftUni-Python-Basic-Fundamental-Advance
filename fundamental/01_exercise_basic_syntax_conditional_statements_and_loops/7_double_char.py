reworked_new_string = ""

while True:
    new_string = input()

    if new_string == "End":
        break
    elif new_string == "SoftUni":
        continue
    else:
        for char in new_string:
            reworked_new_string += char*2
        print(reworked_new_string)
        reworked_new_string = ""
