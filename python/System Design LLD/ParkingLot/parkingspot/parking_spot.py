from abc import ABC, abstractmethod
from parking_spot_type import ParkingSpotType
from vehicles.vehicle import Vehicle

class ParkingSpot(ABC):
    def __init__(self, parking_spot_id: str, parking_spot_type: ParkingSpotType):
        self._is_spot_available = True
        self._parking_spot_id = parking_spot_id
        self._vehicle = None
        self._parking_spot_type = parking_spot_type

    def is_spot_free(self) -> bool:
        return self._is_spot_available

    def get_parking_spot_type(self) -> ParkingSpotType:
        return self._parking_spot_type

    def get_parking_spot_id(self) -> str:
        return self._parking_spot_id

    def get_vehicle_details(self) -> Vehicle:
        return self._vehicle

    def assign_vehicle_to_spot(self, vehicle: Vehicle):
        if not self._is_spot_available:
            raise ValueError(f"No spots are available for {vehicle.get_vehicle_type()}")
        self._vehicle = vehicle
        self._is_spot_available = False

    def vacate_vehicle_from_spot(self):
        self._vehicle = None
        self._is_spot_available = True
