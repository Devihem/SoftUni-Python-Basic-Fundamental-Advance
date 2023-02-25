random_location_string = input()
folders_in_list = random_location_string.split("\\")
file_name, file_extension = folders_in_list[-1].split(".")
print(f"File name: {file_name}\nFile extension: {file_extension}")