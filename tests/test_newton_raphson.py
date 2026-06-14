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

from newton_raphson import NewtonRaphsonSolver


def test_newton_raphson_output():

    ybus = np.array([
        [10, -5],
        [-5, 10]
    ], dtype=complex)

    solver = NewtonRaphsonSolver(ybus)

    voltages, angles, iterations = solver.solve()

    assert len(voltages) == 2
    assert len(angles) == 2
    assert iterations > 0