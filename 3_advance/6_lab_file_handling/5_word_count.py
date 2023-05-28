with open("6_zadacha.py", "w") as file:
    file.write('x = "THIS IS AWSOME"')
    file.write("\nfor _ in range(100):\n    print(x)")
    file.write("\nTest = 0")
    print(open("6_zadacha.py").readlines)