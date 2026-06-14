import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from ybus_builder import YBusBuilder


def test_ybus_matrix_creation():

    builder = YBusBuilder(
        "data/sample_line_data.csv"
    )

    ybus = builder.build()

    assert ybus.shape[0] == ybus.shape[1]
    assert ybus.shape[0] > 0