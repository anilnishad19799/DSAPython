from Interface.sportdriveinterface import SportDrive
from vehicle import Vehicle

class SportVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportDrive())
