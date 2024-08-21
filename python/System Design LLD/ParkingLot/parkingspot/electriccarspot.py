from parking_spot import ParkingSpot
from parking_spot_type import ParkingSpotType

class ElectricCarSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, ParkingSpotType.ELECTRIC_CAR)
