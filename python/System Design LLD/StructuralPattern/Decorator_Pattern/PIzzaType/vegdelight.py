import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from basepizza import BasePizza
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class VegDelight(BasePizza):
    def cost(self):
        return 120
