from enums.Direction import Direction
from interfaces.Button import Button

class HallButton(Button):
    def __init__(self, status, direction) -> None:
        self.status = status
        self.direction = direction

    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction

    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

    def is_pressed(self) -> bool:
        return self.status
    
    def press(self) -> bool:
        self.status = not self.status 
        return self.status
