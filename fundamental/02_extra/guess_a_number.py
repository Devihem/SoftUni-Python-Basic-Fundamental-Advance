import random
number_to_be_guessed = random.randint(1, 100)
counter = 0

print("Guess the number game in range 1-100")
while True:
    user_guess = input("Guess the number:  ")
    if not user_guess.isdigit():
        print("Enter a digit number !")
        continue
    else:
        user_guess = int(user_guess)
    counter += 1
    if user_guess == number_to_be_guessed:
        if counter == 1:
            print("Bull-Eye")
            break
        else:
            print("Good Job. You guess it!")
            break
    elif user_guess > number_to_be_guessed:
        print(" Too High ")
    else:
        print(" Too Low ")
