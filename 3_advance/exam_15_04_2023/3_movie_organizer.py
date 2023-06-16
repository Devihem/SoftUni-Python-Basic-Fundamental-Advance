import os


def movie_organizer(*args):
    movie_dict = {}

    for movie, genre in args:
        if genre not in movie_dict:
            movie_dict[genre] = []
        movie_dict[genre].append(movie)

    sorted_list = sorted(movie_dict.items(), key=lambda k: (-len(k[1]), k[0]))
    final_list = []

    for genre_final, movie_list in sorted_list:
        final_list.append(genre_final + ' - ' + str(len(movie_list)))
        for movie_final in sorted(movie_list):
            final_list.append('* ' + movie_final)

    return os.linesep.join(final_list)


print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
