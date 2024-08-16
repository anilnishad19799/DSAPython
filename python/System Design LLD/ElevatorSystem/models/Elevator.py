from enums.ElevatorNumber import ElevatorNumber
from enums.FloorNumber import FloorNumber
from enums.Direction import Direction
from models.Door import Door
from models.InsidePannel import InsidePannel
from models.Display import Display

class Elevator:
    def __init__(self, elevator_number=None, door=None, inside_pannel=None, display=None, current_floor_number=None, current_direction=None):
        self.elevator_number = elevator_number
        self.door = door
        self.inside_pannel = inside_pannel
        self.display = display
        self.current_floor_number = current_floor_number
        self.current_direction = current_direction

    def get_elevator_number(self):
        return self.elevator_number

    def set_elevator_number(self, elevator_number):
        self.elevator_number = elevator_number

    def get_door(self):
        return self.door

    def set_door(self, door):
        self.door = door

    def get_inside_pannel(self):
        return self.inside_pannel

    def set_inside_pannel(self, inside_pannel):
        self.inside_pannel = inside_pannel

    def get_display(self):
        return self.display

    def set_display(self, display):
        self.display = display

    def get_current_floor_number(self):
        return self.current_floor_number

    def set_current_floor_number(self, current_floor_number):
        self.current_floor_number = current_floor_number

    def get_current_direction(self):
        return self.current_direction

    def set_current_direction(self, current_direction):
        self.current_direction = current_direction