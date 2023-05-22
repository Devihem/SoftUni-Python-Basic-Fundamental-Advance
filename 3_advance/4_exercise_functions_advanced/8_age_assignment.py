def age_assignment(*args, **kwargs):
    result = []
    kwargs = sorted(kwargs.items())

    for key, value in kwargs:
        for name in args:
            if name.startswith(key):
                print_name = name
                age = value
                result.append(f"{print_name} is {age} years old.")

    return '\n'.join(result)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
