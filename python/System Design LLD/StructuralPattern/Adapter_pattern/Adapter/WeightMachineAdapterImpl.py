import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Adaptee import WeightMachine
from WeightMachineAdapter import WeightNachineAdapter
from Adaptee.WeightMachine import WeightMachine

class WeightMachineAdapterImpl(WeightNachineAdapter):

    def __init__(self, weight_machine:WeightMachine):
        self.weight_machine = weight_machine

    def getWeightInKg(self):
        weightinpound = self.weight_machine.getWeightInPound()
        weightinkg = weightinpound * .45
        return weightinkg
