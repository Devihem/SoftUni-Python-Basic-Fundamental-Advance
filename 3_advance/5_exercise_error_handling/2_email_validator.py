"""
File: 2_email_validator.py
Exercise: 14 - Error Handling
Problem: 2 - Email Validator
Author: Ivaylo Stoyanov - Devihem

Description: Exercise provided by SoftUni. In this task, we must write a
program in which we are receiving emails as input from the user and our program
must return the state if the email is Valid based on specific conditions and
raises custom exceptions for various errors. The exact conditions of how it must
work and the input data can be found in the exercise files provided on the SoftUni platform:
https://softuni.bg/trainings/4106/python-advanced-may-2023#lesson-54870
"""

import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtError(Exception):
    pass


# Main parameters for email validation. The length may be change or more domain can be added if is needed.
name_min_len = 4
valid_domains = ['com', 'org', 'net', 'bg']

# Welcome screen - Print
print(' ----------------------------------------------------------'
      '\n|      Welcome - this is basic e-Mail validator.           |'
      '\n|      To STOP the program type "End"                      |'
      '\n|      To see all conditions for VALID e-Mail type "Help"  |'
      '\n ----------------------------------------------------------\n')

# While loop with break command  [user_input == "End"].
while True:

    # Commands and Emails input.
    user_input = input('\nEnter your e-Mail in the valid format -  [user_name][@][***][.][domain]'
                       '\ne-Mail : ')

    # Break the loop and print final message.
    if user_input == 'End':
        print("\nProgram terminated. Thank you for using the email validator.")
        break

    # Extra command added to help the user understand all validations and conditions.
    if user_input == 'Help':
        print('\n\n*************************************************************'
              '***************************************************************'
              '\n* [user_name] - must contain [a-z . _ 0-9] five or more times'
              '                                                              *'
              '\n* [@] - symbol at must be only one                           '
              '                                                              *'
              '\n* [***] - at least one [a-z . _ 0-9]                         '
              '                                                              *'
              '\n* [.] - symbol dot must be only one                          '
              '                                                              *'
              '\n* [domain] - the possible domains are [com, net, org, bg]    '
              '                                                              *'
              '\n* Some of this restrictions are only for this specific task '
              'and they are may be different from the global email policy     *'
              '\n*************************************************************'
              '***************************************************************\n')

    # Regex used to collect the information from user_input.
    # email_match have 3 groups so every error raise to may be call
    regex_pattern_email = r'^([\w]*[\.]*[\w]*)([@]*)[\w]*[\.]([a-z]*)$'
    email_match = re.findall(regex_pattern_email, user_input)

    try:
        # email_match groups [0] contain the name, and we take the len.
        len_email_name = len(email_match[0][0])

        # email_match groups [1] contain all @ symbols in the right place, and we count them.
        counts_ats_symbol = len(email_match[0][1])

        # email_match groups [2] contain the domain name.
        domain_name = email_match[0][2]

        # Exception_1 - Name must be more than 4 characters
        if len_email_name <= name_min_len:
            raise NameTooShortError('Name must be more than 4 characters')

        # Exception_2 - The email must contain symbol @ .
        # Exception_2a - Added one more custom exception for checking if there is only one @.
        if counts_ats_symbol < 1:
            raise MustContainAtSymbolError("Email must contain @")
        elif counts_ats_symbol > 1:
            raise MoreThanOneAtError("Email must contain only one @")

        # Exception_3 - We check if the domain name is in our valid list with domains.
        if domain_name not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    # If the regex is not compleat and the user input is out of the correct format IndexError is raised.
    except IndexError:
        print('Invalid e-Mail format !')

    # If all conditions are passed the e-Mail is valid.
    else:
        print('Email is Valid !')
