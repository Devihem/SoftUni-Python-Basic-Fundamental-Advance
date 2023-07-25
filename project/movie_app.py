from project.user import User
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller


class MovieApp:
    def __init__(self):
        self.movies_collection = []  # obj
        self.users_collection = []  # obj

    def register_user(self, username: str, age: int):
        if self.searching_user_by_username(username):
            raise Exception("User already exists!")

        created_user = User(username, age)
        self.users_collection.append(created_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie_obj):
        username_obj = self.searching_user_by_username(username)

        if not username_obj:
            raise Exception("This user does not exist!")

        if not self.owner_check(movie_obj, username_obj):
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        if movie_obj in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie_obj)
        username_obj.movies_owned.append(movie_obj)
        return f"{username} successfully added {movie_obj.title} movie."

    def edit_movie(self, username: str, movie_obj, **kwargs):
        username_obj = self.searching_user_by_username(username)

        if movie_obj not in self.movies_collection:
            raise Exception(f"The movie {movie_obj.title} is not uploaded!")

        if not self.owner_check(movie_obj, username_obj):
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        for key, new_value in kwargs.items():
            if key == "title":
                movie_obj.title = new_value
            elif key == "year":
                movie_obj.year = new_value
            elif key == "age_restriction":
                movie_obj.age_restriction = new_value

        return f"{username} successfully edited {movie_obj.title} movie."

    def delete_movie(self, username: str, movie_obj):
        username_obj = self.searching_user_by_username(username)

        if movie_obj not in self.movies_collection:
            raise Exception(f"The movie {movie_obj.title} is not uploaded!")

        if not self.owner_check(movie_obj, username_obj):
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        self.movies_collection.remove(movie_obj)
        username_obj.movies_owned.remove(movie_obj)
        return f"{username} successfully deleted {movie_obj.title} movie."

    def like_movie(self, username: str, movie_obj):
        username_obj = self.searching_user_by_username(username)

        if movie_obj.owner == username_obj:
            raise Exception(f"{username} is the owner of the movie {movie_obj.title}!")

        if movie_obj in username_obj.movies_liked:
            raise Exception(f"{username} already liked the movie {movie_obj.title}!")

        movie_obj.likes += 1
        username_obj.movies_liked.append(movie_obj)
        return f"{username} liked {movie_obj.title} movie."

    def dislike_movie(self, username: str, movie_obj):
        username_obj = self.searching_user_by_username(username)

        if movie_obj not in username_obj.movies_liked:
            raise f"{username} has not liked the movie {movie_obj.title}!"

        movie_obj.likes -= 1
        username_obj.movies_liked.remove(movie_obj)
        return f"{username} disliked {movie_obj.title} movie."

    def display_movies(self):
        result = sorted(self.movies_collection, key=lambda k: (-k.year, k.title))
        result = [movie.details() for movie in result]
        result = [] if not result else result  # Try if its working lol
        return '\n'.join(result)

    def __str__(self):
        result = []

        users = ', '.join([user.username for user in self.users_collection])
        if not users:
            users = "All users: No users."
        else:
            users = "All users: " + users

        movies = ', '.join([movie.title for movie in self.movies_collection])
        if not movies:
            movies = "All movies: No movies."
        else:
            movies = "All movies: " + movies


        return f"{users}\n{movies}"

    # HELPERS ----------------------------------------------------------------------------------

    def searching_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    @staticmethod
    def owner_check(movie_obj, username_obj):
        if movie_obj.owner == username_obj:
            return True
        return False
