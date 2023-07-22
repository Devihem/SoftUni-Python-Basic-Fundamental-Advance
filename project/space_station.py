from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()
