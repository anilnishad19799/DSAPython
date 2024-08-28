from hourlycost import HourlyCost
from parkingspot.parking_spot import ParkingSpotType
from parkinglot import ParkingLot
from parking_ticket import ParkingTicket

class ExitPanel:
    def __init__(self, exit_panel_id: str):
        self._exit_panel_id = exit_panel_id

    def get_exit_panel_id(self) -> str:
        return self._exit_panel_id

    def checkout(self, parking_ticket: ParkingTicket) -> ParkingTicket:
        parking_spot_id = parking_ticket.get_parking_spot_id()
        total_duration_in_hours = self._calculate_duration_in_hours(parking_ticket)
        vacated_spot = ParkingLot.get_instance().vacate_parking_spot(parking_spot_id)

        if vacated_spot is None:
            raise ValueError("Unable to find the Parking Spot for the given ID")

        total_amount = self._calculate_price(vacated_spot.get_parking_spot_type(), total_duration_in_hours)
        parking_ticket.set_amount(total_amount)
        return parking_ticket

    def _calculate_price(self, parking_spot_type: ParkingSpotType, duration: int) -> float:
        cost = HourlyCost().get_cost(parking_spot_type)
        return 1 * cost if duration == 0 else duration * cost

    def _calculate_duration_in_hours(self, parking_ticket: ParkingTicket) -> int:
        end_time = parking_ticket.set_end_time().get_end_time()
        duration_in_ms = abs(parking_ticket.get_start_time().timestamp() - end_time.timestamp())
        return round(duration_in_ms / 3600)  # 36e5 is equivalent to 3600000 milliseconds (1 hour)
