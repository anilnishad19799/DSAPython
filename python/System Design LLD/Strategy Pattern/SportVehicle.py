from Interface import sportdriveinterface
from vehicle import Vehicle

class SportVehicle(Vehicle):
    def __init__(self, driveobj):
        super().__init__(sportdriveinterface())