from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.total_capacity = capacity
        self.total_memory = memory

    def install(self, software: Software):
        if software.capacity_consumption > self.capacity and software.memory_consumption > self.memory:
            raise "Software cannot be installed"
        self.software_components.append(software)

        # !!! - Absurd logic where you install components, but you don't calculate actually any ram or capacity
        # self.memory -= software.memory_consumption
        # self.capacity -= software.capacity_consumption

    def uninstall(self, software: Software):
        self.software_components.remove(software)

        # !!! - Absurd logic where you install components, but you don't calculate actually any ram or capacity
        # self.memory += software.memory_consumption
        # self.capacity += software.capacity_consumption

