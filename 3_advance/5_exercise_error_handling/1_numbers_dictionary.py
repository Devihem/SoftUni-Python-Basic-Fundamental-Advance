"""
File: 1_numbers_dictionary.py
Exercise: 14 - Error Handling
Problem: 1 - Numbers Dictionary
Author: Ivaylo Stoyanov - Devihem

Description: Exercise provided by SoftUni. In this particular problem, we must
fix already written code without changing it generally and add few try/expect
conditions to work correctly. The conditions of how it must work and input data
can be found in the exercise files provided on the SoftUni platform:
https://softuni.bg/trainings/4106/python-advanced-may-2023#lesson-54870.
"""

numbers_dictionary = {}

# Step_1 - Filling up the dictionary - {key:value}: [number name = key] , [number integer = value].
command_line = input()
while command_line != 'Search':  # If command_line is "Search" continue to Step_2.
    try:
        number_as_string = command_line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    command_line = input()

# Step_2 - Searching for specific number in the dictionary
command_line = input()
while command_line != 'Remove':  # If command_line is "Remove" continue to Step_3.
    try:
        searched = command_line
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
    command_line = input()

# Step_3 - Removing items from the dictionary
command_line = input()
while command_line != 'End':  # If command_line is "End" stop the while-loop.
    try:
        searched = command_linew
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')
    command_line = input()

# Step_4 in the end of the program, print the dictionary.
print(numbers_dictionary)
