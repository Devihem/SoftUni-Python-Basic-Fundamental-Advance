from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    def set_min_and_max_speed(self):
        self.MIN_SPEED_LIMIT = 400
        self.MAX_SPEED_LIMIT = 600
