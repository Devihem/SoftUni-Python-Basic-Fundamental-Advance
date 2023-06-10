"""
File: 4_directory_traversal.py
Exercise: 16 - File Handling
Problem: 4 - Directory Traversal
Author: Ivaylo Stoyanov - Devihem
"""

import os


# Function using recursion , for only one layer , can be changed by increasing 'depth'.
def save_extensions(dir_name, depth=0):
    # Level of recursion in depth. Can be increased for user needs.
    if depth > 1:
        return

    # .listdir scan for files and folders in the given location
    files_in_location = os.listdir(dir_name)

    # Going through all files. If the file is with extension after name add it to dictionary.
    for file_type in files_in_location:

        # Specifying the file location for next checks in the correct format
        current_file_location = os.path.join(dir_name, file_type)

        # Using os method .isfile to determinate if its file or not
        if os.path.isfile(current_file_location):

            # making a KEY from the file extension
            file_type = file_type.split('.')[-1]

            # if Key not in dictionary , create it and then append value/name
            if file_type not in files_dict.keys():
                files_dict[file_type] = []
            files_dict[file_type].append(file_type)

        # If .isfile is False  -> the location is Folder. Check the folder for more files.
        else:
            save_extensions(current_file_location, depth + 1)


# While loop , added for better experience if the user input wrong location or an error occur !
while True:

    # Main input for directory , the script is defaultly written for current location of the file.
    directory = input(f"\n* * * * * * * * * * * * * * * * * *\n"
                      f"*  FILE SCANNING SCRIPT - SoftUni *\n"
                      f"* * * * * * * * * * * * * * * * * *\n"
                      f"\nDefault scan file directory set to:   {os.getcwd()}  \n"
                      "For default directory - Press [ENTER] or for custom directory Type Path: ")
    if not directory:
        directory = '.'

    # All founded files in the scanned location =  dictionary - format: {[file_type]: [file_1.... file_n]}
    files_dict = {}

    # Calling the function with and giving value = files path
    # Added try/except for Windows-OS Users [ Except WinError5 ] unresolved Admin rights.
    try:
        save_extensions(directory)
        break
    except WindowsError as error:
        print(f'\nOS-Windows Permission Error! Type: {error}'
              f'\nTo resolve this issue you must change the read-only policy for this directory !')
        continue

# Sorting dictionary key-1 ( alphabet of keys ) , key-2 (alphabet of files)
sorted_files_dict = sorted(files_dict.items(), key=lambda k: (k[0], k[1]))

# Creating/Open the report file.
with open('report.txt', 'w') as report_file:
    # Creating the print format for the task and wrote on report.txt file
    for key, files in sorted_files_dict:
        report_file.write(f'.{key}\n')
        for file in files:
            report_file.write(f'---{file}\n')
    print('\n\nreport.txt File Created !')
