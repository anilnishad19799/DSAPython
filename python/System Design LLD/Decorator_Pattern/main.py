import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from PIzzaType.farmhouse import FarmHouse
from Topping.extracheese import ExtraCheese

if __name__ == "__main__":
    farmhouse_pizza = FarmHouse()
    print(f"The cost of a Farmhouse pizza is: {farmhouse_pizza.cost()}")

    # extra_cheese_farmhouse = ExtraCheese(farmhouse_pizza)
    # print(f"The cost of a Farmhouse pizza with extra cheese is: {extra_cheese_farmhouse.cost()}")
