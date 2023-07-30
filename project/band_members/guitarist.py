from project.band_members.musician import Musician


class Guitarist(Musician):
    POSSIBLE_SKILLS = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
