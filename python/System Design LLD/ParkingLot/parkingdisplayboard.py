from parkingspot.parking_spot_type import ParkingSpotType

class DisplayBoard:
    def display_message(self, parking_spot_type: ParkingSpotType, free_spots: int):
        message = f"{parking_spot_type.value} spots free: {free_spots}"
        print(message)
