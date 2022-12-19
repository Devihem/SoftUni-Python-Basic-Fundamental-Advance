temperature = float(input())
a = temperature

if a < 5.0 or a > 35.0:
    print("unknown")
elif a >= 26 and a <= 35:
    print("Hot")
elif a >= 20.1 and a <= 25.9:
    print("Warm")
elif a >= 15 and a <= 20:
    print("Mild")
elif a >= 12 and a <= 14.9:
    print("Cool")
elif a <= 11.9 and a >= 5.00:
    print("Cold")
