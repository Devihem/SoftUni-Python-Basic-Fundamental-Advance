company_dict = {}
while True:

    system_input = input().split(" -> ")
    if system_input[0] == "End":
        break
    company = system_input[0]
    card_id = system_input[1]

    if company not in company_dict:
        company_dict[company] = card_id
    else:
        company_dict[company] += f"|{card_id}"

for company_print in company_dict:
    temporary_list = []
    for ids in company_dict[company_print].split("|"):
        if ids not in temporary_list:
            temporary_list.append(ids)
    print(company_print)
    [print(f"-- {ids_print}") for ids_print in temporary_list]
