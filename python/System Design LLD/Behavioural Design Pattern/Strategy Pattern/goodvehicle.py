from Interface.normaldriveinterface import NormalDrive
from vehicle import Vehicle

class GoodVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDrive())
