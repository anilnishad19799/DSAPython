from enums.FloorNumber import FloorNumber
from interfaces.Button import Button

class ElevatorButton(Button):
    def __init__(self, status=False, floor_number = None):
        self.status = status
        self.floor_number = floor_number
    
    def get_floor_number(self):
        return self.floor_number
    
    def set_floor_number(self, floor_number):
        self.floor_number = floor_number
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
    
    def is_pressed(self) -> bool:
        return self.status

    def press(self) -> bool:
        self.status = not self.status
        return self.status

    
    
