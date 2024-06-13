from sportVehicle import SportVehicle
from goodvehicle import GoodVehicle
from vehicle import Vehicle
class Main:

    normal_drive_vehicle = Vehicle(SportVehicle().driveobj)
    normal_drive_vehicle.drive()