coded_msg = list(input())
take_list = []
skip_list = []
final_list = []
for item in coded_msg:
    if item.isdigit():
        if len(take_list) > len(skip_list):
            skip_list.append(int(item))
        else:
            take_list.append(int(item))

coded_msg = [x for x in coded_msg if not x.isdigit()]

for step in range(0, len(take_list)):
    taken_index = take_list[step]
    taken_value = coded_msg[:taken_index]
    coded_msg = coded_msg[taken_index:]

    skipped_index = skip_list[step]
    coded_msg = coded_msg[skipped_index:]

    final_list += taken_value

print("".join(final_list))
