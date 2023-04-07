soft_uni_list = input().split("0")
final_look = []
for index, item in enumerate(soft_uni_list):
    working_box = ""
    working_box_2 = ""
    if int(len(item)) < 3:
        continue
    else:
        working_box = item
        for symbol in working_box:
            if symbol == "." or symbol == "✶":
                continue
            else:
                if symbol == " ":
                    symbol = "_"
                working_box_2 += symbol
        working_box = working_box_2.lower()
        final_look.append(working_box)
print(*final_look, sep="")
