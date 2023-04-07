def dwarf_registration(name: str, hat: str, size: int, dw_dict: dict, color_counts_dict: dict):
    dwarf_id = name + ":" + hat
    if dwarf_id not in dw_dict:
        dw_dict[dwarf_id] = 0

        if hat not in color_counts_dict:
            color_counts_dict[hat] = 0
        color_counts_dict[hat] += 1

    if size > dw_dict[dwarf_id]:
        dw_dict[dwarf_id] = size
    return dw_dict, color_counts_dict


dwarfs_dict = {}
ccounts_dict = {}
while True:
    command = input()
    if command == "Once upon a time":
        break
    dwarf_name, hat_color, body_size = command.split(" <:> ")
    dwarfs_dict, ccounts_dict = dwarf_registration(dwarf_name, hat_color, int(body_size), dwarfs_dict, ccounts_dict)


sorted_phys = sorted(dwarfs_dict.items(), key=lambda k: -k[1], reverse=False)
new_sorted_list = []
for item in sorted_phys:
    unpack_part = item[0].split(":")
    unpack_part.append(item[1])
    unpack_part.append(ccounts_dict[unpack_part[1]])
    new_sorted_list.append(unpack_part)

final_sorted_list = sorted(new_sorted_list, key=lambda k: (k[2], k[3]), reverse=True)
[print(f"({x[1]}) {x[0]} <-> {x[2]}") for x in final_sorted_list]
