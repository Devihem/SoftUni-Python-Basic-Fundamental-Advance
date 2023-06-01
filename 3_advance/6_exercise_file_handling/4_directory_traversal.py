import os


# Function using recursion , for only one layer , can be changed by increasing 'depth'
def save_extensions(dir_name, depth=0):
    # Level of recursion in depth.
    if depth > 1:
        return

    # File location
    files_in_location = os.listdir(dir_name)

    # Going through all files if the file is with extension after name add it to dictionary
    for file in files_in_location:

        # Specifying the file location for next checks
        current_file_location = os.path.join(dir_name, file)

        # Using os method .isfile to determinate if its file or not
        if os.path.isfile(current_file_location):

            # making a KEY from the file extension
            file_type = file.split('.')[-1]

            # if Key not in dict , create it and then append value/name
            if file_type not in files_dict.keys():
                files_dict[file_type] = []
            files_dict[file_type].append(file)

        # If .isfile is False  -> the location is Folder. Check the folder for files.
        else:
            save_extensions(current_file_location, depth + 1)


# Main input for directory , the script is defaultly written for current location using '.'
directory = input()

# All founded files' dictionary - format: {[file_type]: [file_1.... file_n]}
files_dict = {}

# Calling the function with and giving value = files path
save_extensions(directory)

# Sorting dictionary key-1 ( alphabet of keys ) , key-2 (alphabet of files)
sorted_files_dict = sorted(files_dict.items(), key=lambda k: (k[0], k[1]))


# Creating/Open the report file.
with open('report.txt', 'w') as report_file:

    # Creating the print format for the task and wrote on report.txt file
    for key, files in sorted_files_dict:
        report_file.write(f'.{key}\n')
        for file in files:
            report_file.write(f'---{file}\n')
