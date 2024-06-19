from abc import ABC, abstractmethod
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class BasePizza:
    @abstractmethod
    def cost(self):
        pass