import random
import time

keyboard_programing_characters = "\\qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=+_)(*^%$#!|{}<>?"
characters_string_to_list = list(keyboard_programing_characters)
starting_random_symbol = "@@@"
print("    PRESS ENTER FOR START \n""            OR      \n""INPUT STOP TO END THE TRAIL")
game_starting_time = time.perf_counter()
game_play_time_seconds = 20
score = 0

while game_starting_time + game_play_time_seconds >= time.perf_counter():

    command = input(":")
    if command.lower() == "stop":
        break
    elif command == starting_random_symbol or starting_random_symbol == "@@@":
        random_symbol_pick = random.sample(characters_string_to_list, 1)
        random_symbol = ''.join(random_symbol_pick)
        score += 1
        print(random_symbol)
    else:
        score -= 1

print(score)
