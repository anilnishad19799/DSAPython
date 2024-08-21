import uuid
from datetime import datetime
from vehicles.vehicle_type import VehicleType

class ParkingTicket:
    def __init__(
        self,
        vehicle_type: VehicleType,
        vehicle_register_number: str,
        parking_floor_id: str,
        parking_spot_id: str
    ):
        self._parking_ticket_id = str(uuid.uuid4())
        self._vehicle_type = vehicle_type
        self._vehicle_register_number = vehicle_register_number
        self._parking_floor_id = parking_floor_id
        self._parking_spot_id = parking_spot_id
        self._start_time = None
        self._end_time = None
        self._amount = None

    def set_start_time(self, current_datetime: datetime = None):
        if current_datetime is None:
            current_datetime = datetime.now()
        self._start_time = current_datetime
        return self

    def get_start_time(self) -> datetime:
        return self._start_time

    def get_end_time(self) -> datetime:
        return self._end_time

    def get_amount(self) -> float:
        return self._amount

    def set_end_time(self, current_datetime: datetime = None):
        if current_datetime is None:
            current_datetime = datetime.now()
        self._end_time = current_datetime
        return self

    def set_amount(self, amount: float):
        self._amount = amount
        return self

    def get_vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    def get_parking_spot_id(self) -> str:
        return self._parking_spot_id

    def get_parking_floor_id(self) -> str:
        return self._parking_floor_id

    def get_vehicle_register_number(self) -> str:
        return self._vehicle_register_number
