"""
File: 3_file_manipulator.py
Exercise: 16 - File Handling
Problem: 3 - File manipulator
Author: Ivaylo Stoyanov - Devihem
"""

import os

# While loop with command 'End' for break
while True:

    # Split the input on to main variables
    # 'command - receiving what action to do'
    # 'data' - receiving the info that left from the input ( file names , string , etc )
    command, *data = input().split('-')

    if command == "End":
        break

    # If the circle doest stop - create variable 'file_name' - used in all commands
    file_name = data[0]

    # Command - CREATE
    if command == "Create":

        # Creating empty file ( in local location / current )
        with open(f'{file_name}', 'w') as new_file:
            new_file.write('')

    # Command - ADD
    elif command == "Add":

        # Variable content used in Add command - collecting the data in string format
        content = data[1]

        # Opening 'file_name' and appending / adding content to the file
        with open(f'{file_name}', 'a') as new_file:

            # Adding extra new - line after every append
            new_file.write(content + '\n')

    # Command REPLACE
    elif command == "Replace":

        # Set the variables  old/new string
        old_string = data[1]
        new_string = data[2]

        # Using try/except. If file does not exist trow an error.
        try:
            # Open 'file_name' with mode +r
            with open(file_name, '+r') as new_file:

                # in the current variable 'text' keep and edit the text with new_string/old_string
                text = new_file.read()
                text = text.replace(old_string, new_string)

                # this is how file is totally replaced in +r mode
                # seek(0,0) then truncate at index(0) and is ready for write.
                new_file.seek(0, 0)
                new_file.truncate(0)
                new_file.write(text)

        except FileNotFoundError:
            print('An error occurred')

    # Command  DELETE
    elif command == "Delete":

        # Using try/except. If file does not exist trow an error.
        try:

            # Deleting the file using os library
            os.remove(file_name)

        except FileNotFoundError:
            print('An error occurred')
