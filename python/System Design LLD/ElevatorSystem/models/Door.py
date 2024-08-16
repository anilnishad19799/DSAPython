from enums.DoorAction import DoorAction

class Door:
    def __init__(self, door_action = None) -> None:
        self.door_action = door_action

    def openDoor(self):
        self.door_action = DoorAction.OPEN
    
    def closeDoor(self):
        self.door_action = DoorAction.CLOSE