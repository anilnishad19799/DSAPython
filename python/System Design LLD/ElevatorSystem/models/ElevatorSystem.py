from enums.Direction import Direction
from enums.FloorNumber import FloorNumber
from models.Elevator import Elevator
from models.Floor import Floor
from threading import Lock

class ElevatorSystem:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ElevatorSystem, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.elevators = []
            self.floors = []
            self.initialized = True

    def get_elevators(self):
        return self.elevators

    def set_elevators(self, elevators):
        self.elevators = elevators

    def get_floors(self):
        return self.floors

    def set_floors(self, floors):
        self.floors = floors

    def request_elevator(self, direction, floor):
        # TODO: Implement elevator dispatch logic
        return None

    def open_door(self, elevator):
        elevator.get_door().open_door()

    def close_door(self, elevator):
        elevator.get_door().close_door()

    def select_floor(self, floor_number, elevator):
        elevator.get_inside_pannel().press_floor_button(floor_number.value)
