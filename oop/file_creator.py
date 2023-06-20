"""
by Devihem
"""

import os
import re

location_name = os.getcwd()
folder_name = input("Place: Lab or Exercise name: ").lower().split("-")
files_name = input("Place: All Task - Raw: ")
pattern = r"[0-9]{1,}\.\s([a-zA-Z\-\s\,]{3,})"
math = re.findall(pattern, files_name)

if len(folder_name) > 1:
    final_folder_name = folder_name[0].replace(" ", "_") + folder_name[1].strip()
else:
    final_folder_name = folder_name[0].replace(" ", "_")

final_folder_name = final_folder_name.replace(" ", "_")
os.mkdir(final_folder_name)

for task in math:
    task = task.lower()
    task = task.replace(" ", "_")
    task = task.replace(",", "_")

    # For LINUX
    # with open(f"{location_name}/{final_folder_name}/{task}.py", 'w') as new_file:

    # For WINDOWS
    with open(f"{location_name}\\{final_folder_name}\\{task}.py", 'w') as new_file:
        new_file.write("")

print("Files created, rename manually if there is any issue.\n"
      "Type of names that will be incorrectly written ( with numbers in the end ):\n"
      "Arena 51, Multiply by 2, Numbers from 1 to 10")
