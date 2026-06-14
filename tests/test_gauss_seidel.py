import sys
import os
import numpy as np

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from gauss_seidel import GaussSeidelSolver


def test_gauss_seidel_returns_solution():

    ybus = np.array([
        [10, -5],
        [-5, 10]
    ], dtype=complex)

    solver = GaussSeidelSolver(ybus)

    voltages, iterations = solver.solve()

    assert len(voltages) == 2
    assert iterations > 0