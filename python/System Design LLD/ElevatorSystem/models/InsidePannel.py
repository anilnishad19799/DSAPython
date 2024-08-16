from enums.FloorNumber import FloorNumber
from enums.DoorAction import DoorAction
from models.ElevatorButton import ElevatorButton
from models.DoorButton import DoorButton
from interfaces.Pannel import Pannel

class InsidePannel(Pannel):
    def __init__(self):
        self.elevator_button_list = [ElevatorButton(False, FloorNumber(i)) for i in range(15)]
        self.door_buttons = [DoorButton(False, DoorAction(i + 1)) for i in range(3)]

    def press_floor_button(self, floor_number):
        if 0 <= floor_number < len(self.elevator_button_list):
            return self.elevator_button_list[floor_number].press()
        return False

    def press_door_button(self, door_number):
        if 0 <= door_number < len(self.door_buttons):
            return self.door_buttons[door_number].press()
        return False
