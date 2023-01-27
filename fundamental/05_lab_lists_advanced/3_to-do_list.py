to_do_list = ["0"] * 10

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    else:
        to_do_list[int(command[0])-1] = str(command[1])

to_do_list = [element for element in to_do_list if element != "0"]
print(to_do_list)
