from typing import List, Optional
from entry_panel import EntryPanel
from exitpanel import ExitPanel
from parkingfloor import ParkingFloor

class ParkingLot:
    _instance = None

    def __init__(self):
        self._parking_floors: List[ParkingFloor] = []
        self._entry_panels: List[EntryPanel] = []
        self._exit_panels: List[ExitPanel] = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def vacate_parking_spot(self, parking_spot_id: str):
        for floor in self._parking_floors:
            for spots in floor.get_list_of_parking_spots().values():
                for spot in spots:
                    if spot.get_parking_spot_id() == parking_spot_id:
                        spot.vacate_vehicle_from_spot()
                        return spot
        return None

    def get_list_of_parking_floors(self) -> List[ParkingFloor]:
        return self._parking_floors

    def get_list_of_entry_panels(self) -> List[EntryPanel]:
        return self._entry_panels

    def get_list_of_exit_panels(self) -> List[ExitPanel]:
        return self._exit_panels
