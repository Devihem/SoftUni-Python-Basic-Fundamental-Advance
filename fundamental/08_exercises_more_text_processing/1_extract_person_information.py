incoming_lines = int(input())

for line in range(incoming_lines):
    string = input()
    name = string[string.index("@") + 1: string.index("|")]
    age = string[string.index("#") + 1: string.index("*")]
    print(f"{name} is {age} years old.")
