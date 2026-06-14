import numpy as np


class TransmissionLossCalculator:
    def __init__(self, powers):
        self.powers = powers

    def calculate(self):
        total_loss = np.sum(np.real(self.powers)) * 0.02

        return total_loss