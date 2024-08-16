import os
import sys

# Get the absolute path of the enums directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
enums_path = os.path.join(project_root, 'enums')

# Add the enums directory to the sys.path
if enums_path not in sys.path:
    sys.path.append(enums_path)

from enums.Direction import Direction
from enums.FloorNumber import FloorNumber

class Display:
    def __init__(self, floor_number=None, direction=None, weight=None) -> None:
        self.floor_number = floor_number
        self.direction = direction
        self.weight = weight
    
    def get_floor_number(self):
        return self.floor_number
    
    def set_floor_number(self, floor_number):
        self.floor_number = floor_number
    
    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction
    
    def get_weight(self):
        return self.weight
    
    def set_weight(self, weight):
        self.weight = weight