from typing import List, Dict, Optional
from parkingdisplayboard import DisplayBoard
from parking_spot import ParkingSpot
from parkingspot.parking_spot_type import ParkingSpotType
from vehicles.vehicle import Vehicle
from vehicles.vehicle_type import VehicleType

class ParkingFloor:
    def __init__(self, parking_floor_id: str):
        self._parking_spots: Dict[ParkingSpotType, List[ParkingSpot]] = {
            ParkingSpotType.Compact: [],
            ParkingSpotType.Motorcycle: [],
            ParkingSpotType.Large: [],
            ParkingSpotType.ElectricCar: [],
        }
        self._parking_floor_id: str = parking_floor_id
        self._display_board: DisplayBoard = DisplayBoard()

    def get_parking_floor_id(self) -> str:
        return self._parking_floor_id

    def get_list_of_parking_spots(self) -> Dict[ParkingSpotType, List[ParkingSpot]]:
        return self._parking_spots

    def get_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        spot_type = self._get_spot_type_for_vehicle(vehicle.get_vehicle_type())
        available_spot = next((spot for spot in self._parking_spots[spot_type] if spot.is_spot_free()), None)
        return available_spot

    def show_display_board(self):
        for spot_type, spots in self._parking_spots.items():
            free_spots = [spot for spot in spots if spot.is_spot_free()]
            self._display_board.display_message(spot_type, len(free_spots))

    def _get_spot_type_for_vehicle(self, vehicle_type: VehicleType) -> ParkingSpotType:
        if vehicle_type == VehicleType.Car:
            return ParkingSpotType.Compact
        elif vehicle_type == VehicleType.Motorcycle:
            return ParkingSpotType.Motorcycle
        else:
            return ParkingSpotType.Large

    def get_in_use_spot_id(self, vehicle_type: VehicleType) -> Optional[List[ParkingSpot]]:
        spot_type = self._get_spot_type_for_vehicle(vehicle_type)
        occupied_spots = [spot for spot in self._parking_spots[spot_type] if not spot.is_spot_free()]
        return occupied_spots

    def can_park(self, vehicle: Vehicle) -> bool:
        spot_type = self._get_spot_type_for_vehicle(vehicle.get_vehicle_type())
        return bool(self._parking_spots.get(spot_type))
