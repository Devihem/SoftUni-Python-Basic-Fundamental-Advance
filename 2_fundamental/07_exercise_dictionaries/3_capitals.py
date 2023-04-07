countries_list = input().split(", ")
capitols_list = input().split(", ")
ziped_dict = dict(zip(countries_list, capitols_list))
[print(f"{key} -> {ziped_dict[key]}") for key in ziped_dict]