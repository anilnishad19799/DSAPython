from parkinglot import ParkingLot
from parking_ticket import ParkingTicket
from vehicles.vehicle import Vehicle

class EntryPanel:
    def __init__(self, entry_panel_id: str):
        self._entry_panel_id = entry_panel_id

    def get_entry_panel_id(self) -> str:
        return self._entry_panel_id

    def get_parking_ticket(self, vehicle: Vehicle) -> ParkingTicket:
        parking_floor = next(
            (floor for floor in ParkingLot.get_instance().get_list_of_parking_floors()
            if floor.can_park(vehicle)), None
        )

        if parking_floor is None:
            raise ValueError(f"Parking is unsupported for this {vehicle.get_vehicle_type()} type")

        spot = parking_floor.get_available_spot(vehicle)
        if spot is None:
            raise ValueError(f"No spots are available for {vehicle.get_vehicle_type()}")

        ticket = self._generate_parking_ticket(
            vehicle,
            parking_floor.get_parking_floor_id(),
            spot.get_parking_spot_id()
        )

        spot.assign_vehicle_to_spot(vehicle)
        return ticket

    def _generate_parking_ticket(self, vehicle: Vehicle, parking_floor_id: str, parking_spot_id: str) -> ParkingTicket:
        return ParkingTicket(
            vehicle.get_vehicle_type(),
            vehicle.get_vehicle_register_number(),
            parking_floor_id,
            parking_spot_id
        ).set_start_time()
