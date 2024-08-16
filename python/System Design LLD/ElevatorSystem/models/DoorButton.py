from enums.DoorAction import DoorAction
from interfaces.Button import Button


class DoorButton(Button):
    def get_door_action(self, status = False, door_action = None):
        self.door_action = door_action
        self.status = status
    
    def get_door_action(self):
        return self.get_door_action
    
    def set_door_action(self, door_action):
        self.door_action = door_action
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
    
    def is_pressed(self) -> bool:
        return self.status

    def press(self) -> bool:
        self.status = not self.status
        return self.status

