x = float(input())

while x >= 0:
    x = x*2
    print(f"Result: {x:.2f}")
    x = float(input())
if x < 0:
    print("Negative number!")