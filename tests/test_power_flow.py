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

from power_flow import PowerFlowCalculator


def test_power_flow_calculation():

    ybus = np.array([
        [10, -5],
        [-5, 10]
    ], dtype=complex)

    voltages = np.array([
        1 + 0j,
        1 + 0j
    ])

    calculator = PowerFlowCalculator(
        ybus,
        voltages
    )

    results = calculator.calculate()

    assert "currents" in results
    assert "powers" in results