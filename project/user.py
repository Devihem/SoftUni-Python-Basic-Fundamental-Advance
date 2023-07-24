class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []  # obj
        self.movies_owned = []  # obj

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies_result = [] # TODO
        if not liked_movies_result:
            liked_movies_result = ["No movies liked."]

        owned_movies_result = [] # TODO
        if not owned_movies_result:
            owned_movies_result = ["No movies owned."]

        return f"Username: {self.username}, Age: {self.age}\n" \
               "Liked movies:\n" \
               f"{liked_movies_result}" \
               "Owned movies:" \
               f"{owned_movies_result}"
