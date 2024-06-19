import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from basepizza import BasePizza

class ToppingDecorator(BasePizza):
    def __init__(self, base_pizza):
        self._base_pizza = base_pizza
