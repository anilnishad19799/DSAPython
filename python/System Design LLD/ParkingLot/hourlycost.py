from parkingspot.parking_spot import ParkingSpotType

class HourlyCost:
    def __init__(self):
        self._hourly_costs = {
            ParkingSpotType.Compact: 25,
            ParkingSpotType.Disabled: 15,
            ParkingSpotType.ElectricCar: 35,
            ParkingSpotType.Large: 45,
            ParkingSpotType.Motorcycle: 15,
        }

    def get_cost(self, parking_spot_type: ParkingSpotType) -> int:
        if parking_spot_type in self._hourly_costs:
            return self._hourly_costs[parking_spot_type]
        else:
            raise ValueError(f"Hourly cost is not associated with {parking_spot_type} type")
