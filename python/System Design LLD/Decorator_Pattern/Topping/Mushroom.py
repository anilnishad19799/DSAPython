import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from toppingdecorator import ToppingDecorator

class Mushroom(ToppingDecorator):
    def __init__(self, base_pizza):
        super().__init__(base_pizza)

    def cost(self):
        return self._base_pizza.cost() + 15
