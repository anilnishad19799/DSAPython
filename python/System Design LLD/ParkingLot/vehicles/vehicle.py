from abc import ABC, abstractmethod
from vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(self, vehicle_register_number: str, vehicle_type: VehicleType):
        self._register_number = vehicle_register_number
        self._type = vehicle_type

    def get_vehicle_type(self) -> VehicleType:
        return self._type

    def get_vehicle_register_number(self) -> str:
        return self._register_number
