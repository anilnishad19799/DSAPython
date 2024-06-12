from Interface.driveinterface import DriveInterface

class Vehicle:
    
    def __init__(self, driveobj):
        self.driveobj = driveobj

        def drive(self):
            self.driveobj.drive()