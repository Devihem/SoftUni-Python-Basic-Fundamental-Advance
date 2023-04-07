colored_eggs_loop = int(input())

red_eggs_counter = 0
orange_eggs_counter = 0
blue_eggs_counter = 0
green_eggs_counter = 0
max_colour = ""

for i in range(0, colored_eggs_loop):
    egg_color = input()

    if egg_color == "red":
        red_eggs_counter += 1
    elif egg_color == "orange":
        orange_eggs_counter += 1
    elif egg_color == "blue":
        blue_eggs_counter += 1
    elif egg_color == "green":
        green_eggs_counter += 1

all_eggs_color = [red_eggs_counter, orange_eggs_counter, blue_eggs_counter, green_eggs_counter]

if red_eggs_counter == max(all_eggs_color):
    max_colour = "red"
elif green_eggs_counter == max(all_eggs_color):
    max_colour = "green"
elif blue_eggs_counter == max(all_eggs_color):
    max_colour = "blue"
elif orange_eggs_counter == max(all_eggs_color):
    max_colour = "orange"


print(f"Red eggs: {red_eggs_counter}")
print(f"Orange eggs: {orange_eggs_counter}")
print(f"Blue eggs: {blue_eggs_counter}")
print(f"Green eggs: {green_eggs_counter}")
print(f"Max eggs: {max(all_eggs_color)} -> {max_colour}")
