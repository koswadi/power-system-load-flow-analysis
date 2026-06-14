import numpy as np


class PowerFlowCalculator:
    def __init__(self, ybus, voltages):
        self.ybus = ybus
        self.voltages = voltages

    def calculate(self):
        currents = self.ybus @ self.voltages

        powers = self.voltages * np.conjugate(currents)

        return {
            "currents": currents,
            "powers": powers
        }