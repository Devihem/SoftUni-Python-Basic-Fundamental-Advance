

for _ in range(5):

    try:
        number = int(input())
        if number < 0:
            raise ValueCannotBeNegative
    except ValueCannotBeNegative:
        print(ValueCannotBeNegative)
