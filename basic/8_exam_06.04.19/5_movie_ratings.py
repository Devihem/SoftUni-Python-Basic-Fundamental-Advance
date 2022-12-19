number_movies_loop = int(input())

movie_name = input()
movie_score = float(input())
max_score = movie_score
max_score_name = movie_name
min_score = movie_score
min_score_name = movie_name
total_score = movie_score

for i in range(1, number_movies_loop):
    movie_name = input()
    movie_score = float(input())
    total_score += movie_score

    if movie_score > max_score:
        max_score = movie_score
        max_score_name = movie_name

    elif movie_score < min_score:
        min_score = movie_score
        min_score_name = movie_name

print(f"{max_score_name} is with highest rating: {max_score:.1f}")
print(f"{min_score_name} is with lowest rating: {min_score:.1f}")
print(f"Average rating: {total_score/number_movies_loop:.1f}")
