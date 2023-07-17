from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = [hardware for hardware in System._hardware if hardware_name == hardware.name][0]
        if not searched_hardware:
            return "Hardware does not exist"

        software_buffer_object = ExpressSoftware(name, capacity_consumption, memory_consumption)

        System._software.append(software_buffer_object)
        searched_hardware.install(software_buffer_object)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = [hardware for hardware in System._hardware if hardware_name == hardware.name][0]
        if not searched_hardware:
            return "Hardware does not exist"

        software_buffer_object = LightSoftware(name, capacity_consumption, memory_consumption)

        System._software.append(software_buffer_object)
        searched_hardware.install(software_buffer_object)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        searched_hardware = [hardware for hardware in System._hardware if hardware_name == hardware.name][0]
        searched_software = [software for software in System._software if software_name == software.name][0]
        if searched_hardware and searched_software:
            System._software.remove(searched_software)
            searched_hardware.uninstall(searched_software)

        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory_hardware = sum([hardware.total_memory for hardware in System._hardware])
        total_capacity_hardware = sum([hardware.total_capacity for hardware in System._hardware])
        total_memory_software = sum([software.memory_consumption for software in System._software])
        total_capacity_software = sum([software.capacity_consumption for software in System._software])

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_memory_software} / {total_memory_hardware}\n" \
               f"Total Capacity Taken: {total_capacity_software} / {total_capacity_hardware}"

    @staticmethod
    def system_split():
        print_result = []
        for hardware in System._hardware:

            express_soft_count = sum([1 for soft in hardware.software_components if soft.software_type == 'Express'])
            light_soft_count = sum([1 for soft in hardware.software_components if soft.software_type == 'Light'])
            soft_total_memory = sum([soft.memory_consumption for soft in hardware.software_components])
            soft_total_capacity = sum([soft.capacity_consumption for soft in hardware.software_components])
            soft_all_names = ', '.join([soft.name for soft in hardware.software_components])

            if not soft_all_names:
                soft_all_names = None

            result = f"Hardware Component - {hardware.name}\n" \
                     f"Express Software Components: {express_soft_count}\n" \
                     f"Light Software Components: {light_soft_count}\n" \
                     f"Memory Usage: {soft_total_memory} / {hardware.total_memory}\n" \
                     f"Capacity Usage: {soft_total_capacity} / {hardware.total_capacity}\n" \
                     f"Type: {hardware.hardware_type}\n" \
                     f"Software Components: {soft_all_names}"

            print_result.append(result)

        return '\n'.join(print_result)
