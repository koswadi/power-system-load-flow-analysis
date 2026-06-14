import numpy as np


class GaussSeidelSolver:
    def __init__(self, ybus, tolerance=1e-6, max_iter=100):
        self.ybus = ybus
        self.tolerance = tolerance
        self.max_iter = max_iter

    def solve(self):
        n = len(self.ybus)

        voltages = np.ones(n, dtype=complex)

        for iteration in range(self.max_iter):
            previous = voltages.copy()

            for i in range(1, n):
                sigma = 0

                for j in range(n):
                    if j != i:
                        sigma += self.ybus[i, j] * voltages[j]

                voltages[i] = (
                    1 / self.ybus[i, i]
                ) * (-sigma)

            error = np.max(np.abs(voltages - previous))

            if error < self.tolerance:
                return voltages, iteration + 1

        return voltages, self.max_iter