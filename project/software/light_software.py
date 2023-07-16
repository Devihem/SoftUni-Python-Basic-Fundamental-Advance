from software import Software


class LightSoftware(Software):
    def __init__(self, name: str, software_type, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
