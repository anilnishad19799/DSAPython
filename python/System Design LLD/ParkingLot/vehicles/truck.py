from vehicle import Vehicle
from vehicle_type import VehicleType

class Truck(Vehicle):
    def __init__(self, vehicle_register_number: str, vehicle_type: VehicleType):
        super().__init__(vehicle_register_number, vehicle_type)