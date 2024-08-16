from enums.Direction import Direction
from models.HallButton import HallButton
from interfaces.Pannel import Pannel

class OutsidePannel(Pannel):
    def __init__(self):
        self.hall_buttons = [
            HallButton(False, Direction.UP),
            HallButton(False, Direction.DOWN),
            HallButton(False, Direction.IDLE)
        ]

    def move_up(self):
        # Implement the functionality to handle "move up" actions.
        pass

    def move_down(self):
        # Implement the functionality to handle "move down" actions.
        pass
