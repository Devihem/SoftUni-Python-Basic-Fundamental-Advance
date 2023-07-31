from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        # robots_name = 'none' if not self.robots else " ".join([robot.name for robot in self.robots])

        return f"{self.name} Secondary Service:\n" \
               f"Robots: {'none' if not self.robots else ' '.join([robot.name for robot in self.robots])}"
