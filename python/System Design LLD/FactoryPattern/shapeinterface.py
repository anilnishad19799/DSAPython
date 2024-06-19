""" Making Shape interface """
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def draw(self):
        pass