from math import floor
units_loop = int(input())
red = 0
orange = 0
yellow = 0
white = 0
other = 0
black = 0
score = 0

for i in range(0, units_loop):
    ball_color = input()

    if ball_color == "red":
        score += 5
        red += 1
    elif ball_color == "orange":
        score += 10
        orange += 1
    elif ball_color == "yellow":
        score += 15
        yellow += 1
    elif ball_color == "white":
        score += 20
        white += 1
    elif ball_color == "black":
        score = floor(score / 2)

        black += 1
    else:
        other += 1

print(f"Total points: {score}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")
