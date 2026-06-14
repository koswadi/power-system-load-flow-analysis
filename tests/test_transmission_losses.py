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

from transmission_losses import (
    TransmissionLossCalculator
)


def test_transmission_loss():

    powers = np.array([
        100 + 0j,
        80 + 0j,
        60 + 0j
    ])

    calculator = (
        TransmissionLossCalculator(
            powers
        )
    )

    loss = calculator.calculate()

    assert loss > 0