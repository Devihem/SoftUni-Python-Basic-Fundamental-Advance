number = float(input())
prefix = ""
extra_prefix = ""

if number == 0:
    prefix = "zero"
elif number > 0:
    prefix = "positive"
    if number < 1:
        extra_prefix = "small "
    elif number > 1000000:
        extra_prefix = "large "
elif number < 0:
    prefix = "negative"
    if number > -1:
        extra_prefix = "small "
    elif number < -1000000:
        extra_prefix = "large "

print(f"{extra_prefix}{prefix}")
