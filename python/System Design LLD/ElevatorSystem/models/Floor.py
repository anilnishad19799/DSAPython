from enums.FloorNumber import FloorNumber

class Floor:
    def __init__(self, floor_number=None, outside_pannel=None):
        self.floor_number = floor_number
        self.outside_pannel = outside_pannel

    def get_floor_number(self):
        return self.floor_number

    def set_floor_number(self, floor_number):
        self.floor_number = floor_number

    def get_outside_pannel(self):
        return self.outside_pannel

    def set_outside_pannel(self, outside_pannel):
        self.outside_pannel = outside_pannel