result = 0
current_result = 0
best_movie_name = ""

for i in range(0, 7):
    movie_name = input()

    if movie_name == "STOP":
        break

    for f in movie_name:
        current_result += ord(f)
        if f.islower():
            current_result -= len(movie_name)*2
        elif f.isupper():
            current_result -= len(movie_name)
    if result < current_result:
        result = current_result
        best_movie_name = movie_name
    current_result = 0
else:
    print("The limit is reached.")

print(f"The best movie for you is {best_movie_name} with {result} ASCII sum.")