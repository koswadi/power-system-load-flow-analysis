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
from newton_raphson import NewtonRaphsonSolver


def main():

    print("=" * 50)
    print("NEWTON-RAPHSON LOAD FLOW ANALYSIS")
    print("=" * 50)

    ybus = YBusBuilder(
        "data/sample_line_data.csv"
    ).build()

    solver = NewtonRaphsonSolver(ybus)

    voltages, angles, iterations = (
        solver.solve()
    )

    print("\nVoltage Magnitudes")

    for i, voltage in enumerate(
        voltages,
        start=1
    ):

        print(
            f"Bus {i}: "
            f"{voltage:.4f} p.u."
        )

    print("\nVoltage Angles")

    for i, angle in enumerate(
        angles,
        start=1
    ):

        print(
            f"Bus {i}: "
            f"{angle:.4f} degrees"
        )

    print(
        f"\nConverged in "
        f"{iterations} iterations"
    )


if __name__ == "__main__":
    main()