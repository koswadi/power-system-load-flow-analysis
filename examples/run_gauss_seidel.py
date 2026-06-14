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
from gauss_seidel import GaussSeidelSolver


def main():

    print("=" * 50)
    print("GAUSS-SEIDEL LOAD FLOW ANALYSIS")
    print("=" * 50)

    ybus = YBusBuilder(
        "data/sample_line_data.csv"
    ).build()

    solver = GaussSeidelSolver(
        ybus,
        tolerance=1e-6,
        max_iter=100
    )

    voltages, iterations = solver.solve()

    print("\nVoltage Results")

    for i, voltage in enumerate(
        voltages,
        start=1
    ):

        print(
            f"Bus {i}: "
            f"{abs(voltage):.4f} p.u."
        )

    print(
        f"\nConverged in "
        f"{iterations} iterations"
    )


if __name__ == "__main__":
    main()