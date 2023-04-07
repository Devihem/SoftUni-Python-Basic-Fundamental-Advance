from math import floor

rounds_loop = int(input())
starting_points = int(input())

result = starting_points
win_count = 0

for i in range(0, rounds_loop):
    round_result = input()
    if round_result == "W":
        result += 2000
        win_count += 1
    elif round_result == "F":
        result += 1200
    elif round_result == "SF":
        result += 720

print(f"Final points: {result}")
print(f"Average points: {floor((result-starting_points)/rounds_loop)}")
print(f"{(win_count/rounds_loop)*100:.2f}%")
